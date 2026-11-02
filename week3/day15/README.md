# Day 15: Production-Ready Qdrant RAG Engine

## Overview
A hardened, modular Qdrant RAG system with structured payload filtering, deduplication, and conversational query handling over JSON documents.

## Key Concepts
- **JSON Ingestion**: Ingesting semi-structured knowledge documents with nested metadata attributes.
- **Payload Filtering**: Combining dense vector similarity with boolean metadata filters (category, tags, authors).
- **Grounded Answer Synthesis**: Feeding top matched points into high-capacity LLMs (`gpt-oss-120b`) with source citation.

## Files
- `quadrantfull.py`: Production-grade Qdrant pipeline script with clean error handling and query parsing.
- `knowledge.json`: Structured knowledge dataset.
- `main.py`: Entry point.

## Running
```bash
uv run quadrantfull.py
```
