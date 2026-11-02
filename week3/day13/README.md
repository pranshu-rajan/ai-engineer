# Day 13: End-to-End Vector RAG Pipeline

## Overview
Building a complete end-to-end vector RAG pipeline from scratch. Chunks documents, indexes embeddings in an in-memory NumPy vector space, retrieves top-$k$ relevant chunks for incoming queries, and generates grounded answers.

## Key Concepts
- **Text Chunking**: Breaking documents into coherent, context-preserving passages.
- **Top-$K$ Nearest Neighbor Retrieval**: Ranking document vectors by cosine similarity against the query vector.
- **Context Injection**: Constructing the augmented prompt dynamically with retrieved references.

## Files
- `full_rag.py`: Complete chunking, embedding, vector ranking, and grounded generation pipeline.
- `main.py`: Entry point.

## Running
```bash
uv run full_rag.py
```
