# Week 4: Restaurant Agent with LangGraph StateMachine

## Overview
A production-grade stateful agent managing a multi-stage restaurant order lifecycle built with **LangGraph**. Demonstrates cyclic state machines, conditional routing, stock validation, retry mechanisms, and error recovery.

## Architecture & State Machine Flow
```
[User Input] --> [LLM Brain] --> [Order Confirm]
                                       |
                                       v
                                 [Cook in Kitchen]
                                       |
                                       v
                                 [Serve to Table] --> [End]
```
- **State Schema (`TypedDict`)**: Tracks messages, order details, inventory status, retry counters, and stage status.
- **Resilient Fallbacks**: If dishes are out of stock (e.g. Pasta = 0) or kitchen fails, the agent retries with exponential limits and guides the customer politely.

## Files
- `main.py`: LangGraph StateGraph definition, node functions (`order_confirm`, `cook`, `serve`), and interactive CLI loop.
- `test_scenarios.py`: Automated scenario testing script simulating various user interactions.
- `prompt.md`: System prompt instructions and boundary conditions.

## Running
```bash
uv run main.py
```
Or run the scenario test suite:
```bash
uv run test_scenarios.py
```
