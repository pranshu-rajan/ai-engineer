# Day 9: Streaming LLM Responses

## Overview
Implementing Server-Sent Events (SSE) and token-by-token streaming from LLM APIs to achieve near-instantaneous Time-to-First-Token (TTFT) and improve user experience.

## Key Concepts
- **Streaming API**: Consuming response deltas over HTTP chunks instead of waiting for full generation.
- **Buffer & Delta Handling**: Flushing tokens directly to standard output as they arrive.
- **Latency Optimization**: Perceived latency drops from several seconds to < 300ms.

## Files
- `streaming.py`: Streaming LLM response consumer with delta chunk printing.
- `main.py`: Entry point.

## Running
```bash
uv run streaming.py
```
