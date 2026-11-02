# Day 7: ReAct Pattern & Reasoning Loops (From Scratch)

## Overview
Building the **ReAct (Reason + Act)** pattern from scratch without external agent frameworks. The LLM alternates between Thought, Action, and Observation loops to use tools and answer complex multi-step queries.

## Key Concepts
- **ReAct Architecture**:
  - `Thought`: Model reasons about what step to take next.
  - `Action`: Model calls a specific tool (e.g. `get_product_price`, `calculator`).
  - `Observation`: The environment executes the tool and injects the output back into the message history.
- **Stop Sequences & Regex Parsing**: Extracting tool names and arguments reliably from LLM text generations.

## Files
- `react_chain.py`: Complete implementation of a ReAct agent with tools for product pricing and arithmetic calculation.
- `main.py`: Entry point.

## Running
```bash
uv run react_chain.py
```
