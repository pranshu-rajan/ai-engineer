# Day 3: Tokenization & Context Windows

## Overview
Understanding the atom of Language Models: Tokens. This module covers counting tokens, analyzing prompt vs. completion usage, token limits, and calculating inference costs.

## Key Concepts
- **Tokens vs. Words**: Average ratio (~1 word ≈ 1.33 tokens in English, higher for Hinglish/code).
- **Context Windows**: Maximum limit of input + output tokens that can be processed in a single call.
- **Cost & Latency Management**: Monitoring `usage.prompt_tokens` and `usage.completion_tokens` returned by the API provider.

## Files
- `tokens.py`: Token calculation, usage inspection, and cost tracking across queries.
- `main.py`: Entry point.

## Running
```bash
uv run tokens.py
```
