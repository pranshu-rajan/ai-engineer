# Day 12: Embeddings & Vector Similarity

## Overview
Moving from naive keyword matching to dense vector embeddings and semantic similarity. Generating vector representations of text using local embedding models and calculating geometric cosine similarity.

## Key Concepts
- **Dense Embeddings**: Transforming strings into high-dimensional numerical vectors capturing semantic meaning.
- **Model**: `all-MiniLM-L6-v2` via `sentence-transformers` (384 dimensions).
- **Vector Math**: Computing cosine similarity using NumPy dot products and Euclidean norms:
  $$\text{sim}(u, v) = \frac{u \cdot v}{\|u\| \|v\|}$$

## Files
- `embed_rag.py`: Generates sentence embeddings and compares semantic proximity between related and unrelated texts.
- `main.py`: Entry point.

## Running
```bash
uv run embed_rag.py
```
