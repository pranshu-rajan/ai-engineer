# Day 14: Vector Database Integration with Qdrant

## Overview
Graduating from in-memory arrays to a production-grade vector database: **Qdrant**. Creating collections, configuring distance metrics, upserting dense vector points with payload metadata, and executing ANN (Approximate Nearest Neighbors) vector queries.

## Key Concepts
- **Vector DB vs. NumPy**: Persistence, filtering on structured metadata (payloads), sub-millisecond HNSW indexing at scale.
- **Collection Management**: Creating collections with specific vector dimensions (e.g. 384) and cosine distance.
- **Payload Indexing**: Attaching raw text and source metadata directly to indexed vectors.

## Files
- `qdrant_day14.py`: Qdrant Cloud client connection, collection initialization, point upsert, and semantic search.
- `knowledge.txt`: Unstructured corporate policy document used as the test knowledge base.
- `main.py`: Entry point.

## Running
```bash
uv run qdrant_day14.py
```
