import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


def load_memory() -> dict:
    if not os.path.exists(MEMORY_FILE):
        return {"user_name": None, "facts": [], "created_at": None}
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {"user_name": None, "facts": [], "created_at": None}


def save_memory(memory: dict):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def remember_fact(fact: str):
    memory = load_memory()
    if fact not in memory["facts"]:
        memory["facts"].append(fact)
        memory["last_updated"] = datetime.now().isoformat()
        save_memory(memory)


def set_user_name(name: str):
    memory = load_memory()
    memory["user_name"] = name
    if not memory.get("created_at"):
        memory["created_at"] = datetime.now().isoformat()
    save_memory(memory)


def forget_fact(fact: str):
    memory = load_memory()
    memory["facts"] = [f for f in memory["facts"] if fact.lower() not in f.lower()]
    save_memory(memory)


def clear_memory():
    save_memory({"user_name": None, "facts": [], "created_at": None})


def format_memory_for_prompt() -> str:
    memory = load_memory()
    lines = []
    if memory.get("user_name"):
        lines.append(f"User's name: {memory['user_name']}")
    if memory.get("facts"):
        lines.append("Things you remember about the user:")
        for fact in memory["facts"]:
            lines.append(f"  - {fact}")
    return "\n".join(lines) if lines else ""
