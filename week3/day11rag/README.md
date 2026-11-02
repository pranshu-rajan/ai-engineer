# Day 11: Introduction to Retrieval-Augmented Generation (RAG)

## Overview
Fundamental architecture of Retrieval-Augmented Generation (RAG). Demonstrating why LLMs hallucinate on private or dynamic data and how deterministic retrieval grounds LLM responses in verified facts.

## Key Concepts
- **Limitations of Raw LLMs**: Knowledge cutoff dates, hallucinations on non-public facts, lack of company-specific domain knowledge.
- **The RAG Triad**: Knowledge Base Storage -> Query-based Retrieval -> Context-Injected Generation.
- **Grounding Prompts**: Strict prompt engineering that instructs the model to answer *only* based on the retrieved context.

## Files
- `rag_intro.py`: Minimal dictionary-based retriever linked to an LLM generator.
- `main.py`: Entry point.

## Running
```bash
uv run rag_intro.py
```
