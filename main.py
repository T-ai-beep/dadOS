# ============================================================
#  dadOS v1.0 — MAIN SERVER (Ollama Edition)
#  Runs fully local — no API key, no internet required.
#  Powered by Ollama + llama3.2 on your own machine.
#
#  BEFORE RUNNING:
#  1. Install Ollama: https://ollama.com
#  2. Pull the model: ollama pull llama3.2
#  3. Start Ollama:   ollama serve
#  4. Run dadOS:      python main.py
# ============================================================

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import httpx
import uvicorn
import re
import os

load_dotenv()

from config import (
    NAME, VERSION, MODEL, TEMPERATURE, MAX_TOKENS,
    WEATHER_ENABLED, OLLAMA_BASE_URL
)
from prompt_builder import build_system_prompt
from memory import (
    load_memory, set_user_name, remember_fact,
    forget_fact, clear_memory, format_memory_for_prompt
)
from tools.weather import get_weather, format_weather

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

conversation_history = []


# ── OLLAMA CHAT ────────────────────────────────────────────

async def chat_with_ollama(system: str, messages: list) -> str:
    """
    Send a conversation to Ollama and get a response.

    CONCEPT: How local AI works
    Instead of sending your message to a cloud server, Ollama runs the model
    right on your computer. Same HTTP call, never leaves your machine.
    """
    ollama_messages = [{"role": "system", "content": system}]
    ollama_messages.extend(messages)

    payload = {
        "model": MODEL,
        "messages": ollama_messages,
        "stream": False,
        "options": {
            "temperature": TEMPERATURE,
            "num_predict": MAX_TOKENS,
        }
    }

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{OLLAMA_BASE_URL}/api/chat",
                json=payload
            )
            data = response.json()
            return data["message"]["content"]

    except httpx.ConnectError:
        return (
            "⚠ Cannot connect to Ollama. Make sure it's running:\n\n"
            "  ollama serve\n\n"
            "And that you've pulled the model:\n\n"
            "  ollama pull llama3.2"
        )
    except Exception as e:
        return f"⚠ Ollama error: {str(e)}"


# ── MEMORY COMMAND PARSER ───────────────────────────────────

def parse_memory_command(message: str) -> dict | None:
    msg = message.lower().strip()

    name_match = re.search(r"my name is ([a-zA-Z]+)", msg)
    if name_match:
        return {"type": "set_name", "value": name_match.group(1).title()}

    remember_match = re.search(r"remember that (.+)", msg)
    if remember_match:
        return {"type": "remember", "value": remember_match.group(1)}

    forget_match = re.search(r"forget (?:that )?(.+)", msg)
    if forget_match:
        return {"type": "forget", "value": forget_match.group(1)}

    return None


# ── ROUTES ─────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r") as f:
        return f.read()


@app.get("/status")
async def status():
    memory = load_memory()
    return JSONResponse({
        "name": NAME,
        "version": VERSION,
        "model": MODEL,
        "engine": "ollama",
        "user_name": memory.get("user_name") or "unknown",
        "memory_facts": len(memory.get("facts", [])),
    })


@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return JSONResponse({"error": "No message provided"}, status_code=400)

    # Handle memory commands directly — no model needed
    memory_cmd = parse_memory_command(user_message)
    if memory_cmd:
        if memory_cmd["type"] == "set_name":
            set_user_name(memory_cmd["value"])
            return JSONResponse({
                "response": f"Got it — I'll remember your name is {memory_cmd['value']}.",
                "version": VERSION
            })
        elif memory_cmd["type"] == "remember":
            remember_fact(memory_cmd["value"])
            return JSONResponse({
                "response": f"Noted. I'll remember that {memory_cmd['value']}.",
                "version": VERSION
            })
        elif memory_cmd["type"] == "forget":
            forget_fact(memory_cmd["value"])
            return JSONResponse({
                "response": "Done. Forgotten.",
                "version": VERSION
            })

    # Fetch live weather if weather-related
    weather_context = ""
    weather_keywords = ["weather", "temperature", "rain", "sunny", "forecast", "cold", "hot", "outside"]
    if WEATHER_ENABLED and any(kw in user_message.lower() for kw in weather_keywords):
        weather_data = await get_weather()
        weather_context = format_weather(weather_data)

    # Build system prompt fresh on every request
    memory_str = format_memory_for_prompt()
    system = build_system_prompt(weather_context=weather_context)
    if memory_str:
        system += f"\n\n━━━ WHAT YOU REMEMBER ━━━\n{memory_str}\n"

    # Send to Ollama
    conversation_history.append({"role": "user", "content": user_message})
    assistant_message = await chat_with_ollama(system, conversation_history)
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return JSONResponse({
        "response": assistant_message,
        "version": VERSION,
        "model": MODEL,
        "engine": "ollama"
    })


@app.post("/reset")
async def reset():
    conversation_history.clear()
    return JSONResponse({"status": "Session cleared"})


@app.post("/memory/clear")
async def memory_clear():
    clear_memory()
    return JSONResponse({"status": "Memory wiped"})


@app.get("/memory")
async def get_memory():
    return JSONResponse(load_memory())


@app.get("/health")
async def health():
    """Check if Ollama is reachable and show available models."""
    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            res = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            models = [m["name"] for m in res.json().get("models", [])]
            return JSONResponse({
                "ollama": "online",
                "available_models": models,
                "active_model": MODEL
            })
    except Exception:
        return JSONResponse({
            "ollama": "offline",
            "message": "Run: ollama serve"
        }, status_code=503)


# ── START ──────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"\n🤖 {NAME} v{VERSION} starting up...")
    print(f"   Engine : Ollama ({MODEL}) — fully local, no API key needed")
    print(f"   Prereqs: ollama serve  +  ollama pull {MODEL}")
    print(f"   Browser: http://localhost:8000\n")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
