# Week 2 Capstone: HireMeAI

## Overview
**HireMeAI** is an interactive candidate persona backend and resume intelligence system. It parses a candidate's resume (PDF) into strongly-typed Pydantic schemas, and launches an AI avatar that acts on behalf of the candidate during recruiter screening conversations.

## Architecture
1. **Resume Ingestion**: Parses PDF resumes via `pypdf`.
2. **Schema Extraction**: Converts raw resume text into structured Pydantic models (`Resume`, `Experience`).
3. **Conversational Agent**: An AI representative grounded strictly in the candidate's verified background, projects, and work history.
4. **FastAPI Backend**: Exposes REST endpoints to query candidate insights and engage in simulated recruiter interviews.

## Tech Stack
- **FastAPI**: Lightweight, asynchronous web framework.
- **Groq API**: High-throughput LLM inference (`gpt-oss-120b`).
- **Pydantic**: Data validation and strict JSON schema generation.
- **PyPDF**: PDF document parsing.

## Files
- `backend/main.py`: Complete FastAPI application with resume extraction and recruiter chat endpoints.
- `backend/my_resume.pdf`: Sample candidate resume for testing.
- `main.py`: Entry point.

## Running
```bash
cd week2/hiremeai
uv run fastapi dev backend/main.py
```
API docs available at: `http://localhost:8000/docs`
