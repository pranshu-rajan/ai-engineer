# Week 4: RAG Evaluation & LLM-as-a-Judge

## Overview
A comprehensive evaluation suite for RAG systems. Moving beyond subjective testing to quantitative metrics measuring retrieval quality and generation faithfulness using an **LLM-as-a-Judge** framework and Qdrant vector store.

## Metrics Implemented
- **Retrieval Precision**: Ratio of retrieved chunks that are genuinely relevant to the query.
- **Retrieval Recall**: Fraction of golden/ground-truth reference points successfully captured.
- **Answer Faithfulness (Hallucination Detection)**: Verifying whether every claim in the generated answer is directly supported by retrieved context.
- **Answer Relevance**: Ensuring the generated response directly addresses the user's intent without drifting.

## Files
- `rag_evalu.py`: Complete evaluation pipeline (Qdrant collection setup, synthetic query execution, automated LLM judging).
- `knowledge.json`: Ground truth dataset with facts and references.
- `main.py`: Entry point.

## Running
```bash
uv run rag_evalu.py
```
