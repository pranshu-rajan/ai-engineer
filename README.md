# 🚀 AI Engineering Track: Foundations to Production Agents

[![Python 3.12](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Package Manager: uv](https://img.shields.io/badge/Package_Manager-uv-DE5FE9?style=for-the-badge&logo=astral&logoColor=white)](https://github.com/astral-sh/uv)
[![Groq](https://img.shields.io/badge/Inference-Groq_API-F05A28?style=for-the-badge)](https://groq.com)
[![Vector DB: Qdrant](https://img.shields.io/badge/Vector_DB-Qdrant_Cloud-DC244C?style=for-the-badge&logo=qdrant&logoColor=white)](https://qdrant.tech)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-1C3C3C?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)

A hands-on, production-grade learning track and project portfolio documenting my personal journey to mastering **AI & LLM Engineering**.

This repository follows my self-directed curriculum: zero academic fluff, zero superficial wrapper demos, and a constant focus on **evaluation, production constraints, structured schemas, vector search, and autonomous agent loops**.

---

## 📌 Curriculum & Learning Roadmap

| Week | Focus Area | Key Concepts | Capstone / Artifact | Directory |
| :---: | :--- | :--- | :--- | :---: |
| **Week 1** | **LLM Fundamentals & Structured I/O** | Tokenization, temperature, system prompts, context windows, JSON schemas | **Resume Information Extractor** | [`week1/`](week1/) |
| **Week 2** | **Prompt Engineering & Chaining** | ReAct from scratch, few-shot prompting, streaming, sequential pipelines | **HireMeAI Candidate Persona API** | [`week2/`](week2/) |
| **Week 3** | **RAG & Vector Databases** | Semantic embeddings, cosine similarity, Qdrant Cloud HNSW indexing | **YouTube Lecture Timestamp RAG Engine** | [`week3/`](week3/) |
| **Week 4** | **Agents & RAG Evaluation** | Function calling, Tavily search, LLM-as-a-Judge, LangGraph state machines | **Stateful Restaurant Lifecycle Agent** | [`week4/`](week4/) |
| **Week 5** | **Multi-Agent Systems & Integrity** | Hierarchical delegation, persistent notes memory, AST analysis, MOSS | **AI Proctor Code Plagiarism Engine** | [`week5/`](week5/) |
| **Week 6** | **Autonomous Coding Agents** | Tool calling for file inspection, surgical edits, compiler validation, rollback | **Autonomous C++ Bug-Fixing Agent** | [`week6/`](week6/) |

---

## 🌟 Featured Capstone Highlights

### 1. 🎬 [YouTube Lecture Timestamp RAG Engine](week3/ytscraper/)
- **Problem**: Standard RAG applications dump arbitrary text paragraphs without verifiable provenance.
- **Solution**: A production RAG system over technical YouTube lecture playlists that returns concise answers grounded strictly in transcripts, accompanied by **clickable timestamp links that jump directly to the exact second in the lecture video**.
- **Tech Stack**: `faster-whisper` (batched CTranslate2 GPU/CPU transcription), time-window chunking, `BAAI/bge-m3` dense embeddings (1024-dim), **Qdrant Cloud** vector storage, and a **FastAPI + YouTube IFrame API** web interface.

### 2. 🛡️ [AI Proctor — Academic Integrity & Plagiarism Engine](week5/aiproctor/)
- **Problem**: Detecting code plagiarism and unauthorized AI-generated submissions in computer science courses with minimal inference cost.
- **Solution**: A **two-tiered architecture**:
  1. *Free Offline Scan*: Runs MOSS winnowing k-gram hashing for pairwise similarity, AST-based same-bug signature detection, and heuristic AI coding style analysis.
  2. *Escalation Agent*: Only high-suspicion submissions are escalated to an autonomous LLM investigative agent for detailed audit and verdict justification.

### 3. 🤖 [Autonomous C++ Bug-Fixing Agent](week6/codingagent/)
- **Problem**: Resolving codebase bugs from natural language descriptions without human intervention.
- **Solution**: A closed-loop software engineering agent equipped with file system exploration (`search_files`, `search_in_file`, `replace_line`). It diagnoses the problem, applies surgical line replacements, invokes `g++` via subprocess, inspects compiler diagnostics, and automatically rolls back if unresolved within 3 attempts.

### 4. 🍽️ [Stateful Restaurant Order Lifecycle Agent](week4/restproject/)
- **Problem**: Complex workflows fail when modeled as single-shot prompts without retry budgets and state isolation.
- **Solution**: A cyclic state machine built with **LangGraph** modeling `User Input -> Order Confirmation -> Kitchen Cooking -> Table Serving`. Includes inventory stock tracking, retry limits, and friendly conversational fallbacks for out-of-stock items.

### 5. 💼 [HireMeAI Candidate Persona Backend](week2/hiremeai/)
- **Problem**: Generic resumes lack interactivity and fail to answer specific recruiter questions.
- **Solution**: Ingests candidate PDF resumes, extracts structured data into strict Pydantic schemas, and launches an AI avatar that represents the candidate in simulated recruiter screening interviews via FastAPI REST endpoints.

---

## 📂 Repository Structure

```
├── .env.example              # Sample environment template (Groq, Qdrant, Tavily)
├── .gitignore                 # Comprehensive gitignore (hides .env, .venv, caches)
├── README.md                  # Master repository documentation
│
├── week1/                     # LLM Fundamentals & API Mastery
│   ├── day1/                  # Setup, virtual environments, first LLM calls (Notes.md)
│   ├── day2/                  # System prompts & temperature parameter tuning
│   ├── day3/                  # Token counting, context windows, and cost estimation
│   ├── day4/                  # Structured output extraction with Pydantic
│   └── day5/                  # Capstone: Resume Parser (PDF/DOCX -> JSON)
│
├── week2/                     # Prompt Engineering & Pipelines
│   ├── day6/                  # Prompt structure, few-shot prompting, constraints
│   ├── day7/                  # ReAct pattern (Reason + Act loop) from scratch
│   ├── day8/                  # Sequential multi-step LLM chaining
│   ├── day9/                  # Token-by-token streaming responses
│   └── hiremeai/              # Capstone: Candidate Persona & Interview Backend
│
├── week3/                     # Retrieval-Augmented Generation (RAG)
│   ├── day11rag/              # RAG fundamentals & naive dictionary retrieval
│   ├── day12/                 # Dense text embeddings & cosine vector math
│   ├── day13/                 # End-to-end vector retrieval pipeline
│   ├── day14/                 # Qdrant Cloud integration (collections & points)
│   ├── day15/                 # Production Qdrant RAG over structured JSON
│   └── ytscraper/             # Capstone: Full YouTube Transcript RAG with Web UI
│
├── week4/                     # Tool Agents & Evaluation
│   ├── agents/                # Autonomous tool calling (Tavily Search + Calculator)
│   ├── rag_eval/              # Quantitative RAG Evaluation & LLM-as-a-Judge suite
│   └── restproject/           # Capstone: Stateful Restaurant Agent with LangGraph
│
├── week5/                     # Multi-Agent Systems & Code Analysis
│   ├── aiproctor/             # Capstone: MOSS + AST + AI Proctoring system
│   └── multiagent/            # Manager-Worker agent hierarchy with shared memory
│
└── week6/                     # Autonomous Software Engineering
    └── codingagent/           # Capstone: Self-correcting C++ bug repair agent
```

---

## 🛠️ Quickstart & Local Setup

### 1. Prerequisites
- **Python 3.12+**
- **uv** (recommended lightning-fast package manager):
  ```bash
  # Windows (PowerShell)
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  
  # macOS / Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd "AI ENGINEER"
```

### 3. Environment Configuration
Copy the template and configure your API keys:
```bash
cp .env.example .env
```
Fill in the credentials in `.env`:
- `GROQ_API_KEY`: [Groq Console](https://console.groq.com) (free tier available)
- `QDRANT_URL` & `QDRANT_API_KEY`: [Qdrant Cloud](https://cloud.qdrant.io) (free cluster)
- `TAVILY_API_KEY`: [Tavily AI](https://tavily.com) (for search agents)

### 4. Running Any Project
Every subproject is self-contained with its own `pyproject.toml` and dependencies managed via `uv`:

```bash
# Run the Week 3 YouTube RAG web application
cd week3/ytscraper
uv run fastapi dev api/main.py

# Run the Week 5 AI Proctor scan
cd week5/aiproctor
uv run main.py longest_substring

# Run the Week 6 Autonomous Coding Agent
cd week6/codingagent
uv run main.py
```

---

## 💡 Key Engineering Takeaways

1. **Evals Over Vibes**: If you can't measure retrieval precision and response faithfulness with automated test suites, you can't improve it.
2. **Schema Enforcement is Non-Negotiable**: 80% of production LLM pipelines rely on deterministic, structured outputs validated via Pydantic rather than free-form text.
3. **Cost-Aware Architectures**: Always use cheap local algorithms (ASTs, tokenizers, vector math) for pre-filtering, reserving LLM calls for complex reasoning.
4. **Lightweight First**: Build agents with clean loops and explicit tools before jumping into complex multi-agent frameworks.

---

## 📬 Contact & Connect

- **Author**: Pranshu
- **Focus**: AI Engineering / LLM Applications / Agentic Systems
