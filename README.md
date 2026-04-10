# dadOS v1.0

## Setup

**1. Install Ollama**
https://ollama.com

**2. Pull the model**
```bash
ollama pull llama3.2
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run**
```bash
ollama serve
python main.py
```

**5. Open browser**
```
http://localhost:8000
```

---

## Optional: Live weather

Get a free key at https://openweathermap.org/api, then:
```bash
cp .env.example .env
# paste your key into .env
```

---

## Project structure

```
dadOS-v1.0/
├── main.py              # Server — handles all requests
├── config.py            # Personality & settings — start here
├── prompt_builder.py    # Builds the AI's instructions every message
├── memory.py            # Saves facts across sessions
├── tools/
│   └── weather.py       # Live weather tool
├── templates/
│   └── index.html       # The chat UI
├── requirements.txt
└── .env.example
```

**The file to open first:** `config.py` — this is where dadOS's name, topics, and behavior live.

---

## How memory works

```
my name is ___           → dadOS remembers your name
remember that ___        → saves a fact permanently
forget that ___          → removes a fact
```

---

## The Roadmap

### 🟢 Foundation (already built)

| Version | What you do | Concept |
|---------|-------------|---------|
| v0.1 | Change dadOS's name & personality | System prompts |
| v0.2 | Make dadOS remember your name | Context & state |
| v0.3 | Make dadOS an expert on something | Prompt engineering |
| v0.4 | Connect dadOS to a live API | Tool use |
| v0.5 | Make dadOS ask clarifying questions | Prompt chaining |
| v0.6 | Make dadOS respond differently by time of day | Conditional logic |
| v0.7 | Add reset, clear chat, new session | UI basics |
| v0.8 | Style the chat UI | Frontend |
| v0.9 | Make it work on your phone | Responsive design |
| v1.0 | Show dadOS to someone | Milestone |

---

### 🤖 Path 1 — The Agent
*Make dadOS act, not just talk.*

| Version | What you build |
|---------|----------------|
| v1.1 | dadOS can search the web |
| v1.2 | dadOS gives himself a to-do list |
| v1.3 | dadOS completes multi-step tasks |
| v1.4 | dadOS runs on a schedule |
| v1.5 | dadOS browses a website |
| v1.6 | dadOS fills out a form |
| v1.7 | dadOS checks his own work |
| v1.8 | dadOS retries when he fails |
| v1.9 | dadOS logs everything he does |
| v2.0 | dadOS does something useful every day unprompted |

---

### 🧠 Path 2 — The Reasoner
*Make dadOS think harder.*

| Version | What you build |
|---------|----------------|
| v2.1 | dadOS thinks step-by-step before answering |
| v2.2 | dadOS argues both sides of any question |
| v2.3 | dadOS challenges his own first answer |
| v2.4 | dadOS breaks big problems into smaller ones |
| v2.5 | dadOS asks Socratic questions |
| v2.6 | dadOS rates his own confidence |
| v2.7 | dadOS changes his mind when given evidence |
| v2.8 | dadOS explains his reasoning step by step |
| v2.9 | dadOS identifies when he doesn't know something |
| v3.0 | dadOS solves a problem you couldn't solve alone |

---

### 🧬 Path 3 — The Scientist
*Understand how AI actually works.*

| Version | What you build |
|---------|----------------|
| v3.1 | Count how many tokens dadOS uses per message |
| v3.2 | Change the temperature and see what happens |
| v3.3 | Hit the context window limit on purpose |
| v3.4 | Compare two different models side by side |
| v3.5 | Write a system prompt evaluator |
| v3.6 | Understand embeddings — visualize them |
| v3.7 | Build semantic search for dadOS's memory |
| v3.8 | Build a RAG pipeline from scratch |
| v3.9 | Fine-tune a small model on your own data |
| v4.0 | Explain how dadOS thinks to someone else |

---

### 🔗 Path 4 — The Connector
*Connect dadOS to the real world.*

| Version | What you build |
|---------|----------------|
| v4.1 | dadOS fetches live news |
| v4.2 | dadOS reads your calendar |
| v4.3 | dadOS sends a daily briefing email |
| v4.4 | dadOS texts you via WhatsApp or SMS |
| v4.5 | dadOS pulls live sports scores |
| v4.6 | dadOS reads a spreadsheet and answers questions |
| v4.7 | dadOS posts to a platform on your behalf |
| v4.8 | dadOS watches a price and alerts you |
| v4.9 | dadOS connects to your smart home |
| v5.0 | dadOS is wired into your actual life |

---

### 🗃️ Path 5 — The Memory Architect
*Give dadOS real, deep memory.*

| Version | What you build |
|---------|----------------|
| v5.1 | dadOS remembers across sessions (beyond JSON) |
| v5.2 | dadOS stores facts in a real database |
| v5.3 | dadOS can search his own memory |
| v5.4 | Feed dadOS a document — he answers questions |
| v5.5 | dadOS summarizes what he knows about any topic |
| v5.6 | dadOS forgets things you tell him to |
| v5.7 | dadOS organizes memory into categories |
| v5.8 | dadOS retrieves the right memory at the right time |
| v5.9 | dadOS builds a knowledge graph about you |
| v6.0 | dadOS knows you better than Google does |

---

### 👁️ Path 6 — The Multimodal
*Give dadOS eyes, ears, and a voice.*

| Version | What you build |
|---------|----------------|
| v6.1 | dadOS reads an image you send him |
| v6.2 | dadOS describes photos |
| v6.3 | dadOS generates images |
| v6.4 | Talk to dadOS out loud |
| v6.5 | dadOS talks back |
| v6.6 | Full voice conversation with dadOS |
| v6.7 | dadOS reads a PDF and summarizes it |
| v6.8 | dadOS watches a YouTube video and takes notes |
| v6.9 | dadOS can see your screen |
| v7.0 | dadOS has all his senses |

---

### 🎨 Path 7 — The Creative
*Make dadOS generate things.*

| Version | What you build |
|---------|----------------|
| v7.1 | dadOS writes a story in your style |
| v7.2 | dadOS generates images from descriptions |
| v7.3 | dadOS writes music lyrics on demand |
| v7.4 | dadOS generates a logo or icon |
| v7.5 | dadOS creates a slide deck from a prompt |
| v7.6 | dadOS edits images you give it |
| v7.7 | dadOS generates variations of anything |
| v7.8 | dadOS collaborates with you on creative work |
| v7.9 | dadOS has a creative style that's uniquely his |
| v8.0 | dadOS creates something you're proud of |

---

### 📊 Path 8 — The Data Scientist
*Teach dadOS from data.*

| Version | What you build |
|---------|----------------|
| v8.1 | dadOS analyzes a CSV you give him |
| v8.2 | dadOS spots patterns in data |
| v8.3 | dadOS makes simple predictions |
| v8.4 | Train a model to classify something you care about |
| v8.5 | dadOS clusters information automatically |
| v8.6 | dadOS builds a recommendation system |
| v8.7 | dadOS learns your preferences over time |
| v8.8 | dadOS runs a proper experiment |
| v8.9 | dadOS visualizes data beautifully |
| v9.0 | dadOS trained on something you built |

---

### 🔬 Path 9 — The Evaluator
*Measure if dadOS is actually good.*

| Version | What you build |
|---------|----------------|
| v9.1 | Write your first test case for dadOS |
| v9.2 | Build an eval set of 20 questions |
| v9.3 | Score dadOS automatically |
| v9.4 | Compare dadOS v1 vs dadOS v2 |
| v9.5 | Find where dadOS consistently fails |
| v9.6 | Build a red-teaming setup |
| v9.7 | Measure response quality over time |
| v9.8 | Build a benchmark for your use case |
| v9.9 | Catch regressions before they happen |
| v10.0 | dadOS is measurably, provably better |

---

### 🌐 Path 10 — The Orchestrator
*Multiple AIs working together.*

| Version | What you build |
|---------|----------------|
| v10.1 | dadOS talks to a second AI |
| v10.2 | dadOS delegates to a specialist AI |
| v10.3 | dadOS runs a pipeline of AI steps |
| v10.4 | dadOS has a planner and a doer |
| v10.5 | dadOS spawns sub-agents for parallel work |
| v10.6 | dadOS routes questions to the right model |
| v10.7 | dadOS has a critic that reviews the main AI |
| v10.8 | dadOS coordinates 3 AIs at once |
| v10.9 | dadOS manages a full AI workflow |
| v11.0 | dadOS is a system, not just an AI |