# Day 2: System Prompts & Temperature Control

## Overview
Exploration of core LLM generation parameters and role framing. Demonstrates how system prompts condition model behavior and how temperature affects determinism vs. creativity.

## Key Concepts
- **System vs. User Roles**: Establishing behavioral boundaries, persona constraints, and output restrictions before user input.
- **Temperature Parameter**:
  - `temperature = 0`: Deterministic, focused, and greedy token selection (ideal for code, extraction, classification).
  - Higher temperature (`0.7 - 1.2`): Increased randomness and vocabulary diversity (creative writing, brainstorming).

## Files
- `sys_temp.py`: Script demonstrating brand name generation under strict single-word system constraints and zero temperature.
- `main.py`: Entry point and test harness.

## Running
```bash
uv run sys_temp.py
```
