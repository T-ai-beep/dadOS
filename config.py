# ============================================================
#  dadOS CONFIG v1.0 — THIS IS WHERE YOU MAKE ME YOURS
#  Every upgrade you've done so far lives here.
#  This file is the soul of dadOS. Change anything.
# ============================================================

# ── IDENTITY ───────────────────────────────────────────────
NAME        = "dadOS"
VERSION     = "1.0"
USER_NAME   = "Manav"   # ← Your name. Already set.

# ── EXPERT TOPICS ──────────────────────────────────────────
# Things dadOS knows a lot about.
# Add anything you care about — sports, cooking, history, music.
# dadOS will go deep on these topics when they come up.
EXPERT_TOPICS = [
    "artificial intelligence",
    "technology",
    # Add your own:
    # "football",
    # "cooking",
    # "history",
]

# ── TIME-OF-DAY MODES ──────────────────────────────────────
# dadOS adapts his energy based on the time of day.
# You can change the hours and the mood descriptions.
TIME_MODES = {
    "morning":    {"hours": range(5, 12),  "mood": "energetic and focused, ready to start the day"},
    "afternoon":  {"hours": range(12, 17), "mood": "steady and practical, good for getting things done"},
    "evening":    {"hours": range(17, 21), "mood": "relaxed and reflective, winding down"},
    "night":      {"hours": range(21, 24), "mood": "calm and thoughtful, quieter energy"},
    "late_night": {"hours": range(0, 5),   "mood": "minimal and direct, it's late"},
}

# ── CLARIFYING QUESTIONS ───────────────────────────────────
# Topics where dadOS will ask one clarifying question before answering.
CLARIFY_TOPICS = [
    "help",
    "explain",
    "how do i",
    "what should i",
    "recommend",
    "suggest",
    "advice",
    "best way",
]

# ── AI SETTINGS ────────────────────────────────────────────
# Running locally via Ollama — no API key needed.
# Make sure Ollama is running: `ollama serve`
# And the model is pulled: `ollama pull llama3.2`
MODEL       = "llama3.2"
TEMPERATURE = 0.7    # 0.0 = predictable, 1.0 = creative
MAX_TOKENS  = 1024

# Ollama runs locally at this address by default.
OLLAMA_BASE_URL = "http://localhost:11434"

# ── LIVE API TOOLS ─────────────────────────────────────────
# Set WEATHER_API_KEY in your .env file to enable weather.
# Get a free key at: https://openweathermap.org/api
WEATHER_ENABLED = True
DEFAULT_CITY    = "New York"   # ← Change to your city
