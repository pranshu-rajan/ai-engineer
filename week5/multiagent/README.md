# Week 5: Multi-Agent Collaboration & Delegation Architecture

## Overview
A lightweight, multi-agent orchestration architecture built without heavyweight frameworks. Features a **Manager Agent** that decomposes high-level user goals, delegates subtasks to specialized worker agents, persists findings in shared notes, and aggregates the final response.

## Multi-Agent Hierarchy
```
               [Manager LLM]
              /             \
             v               v
    [Search Specialist]   [Maths Specialist]
       (Tavily Search)       (Exact Arithmetic)
             \               /
              v             v
            [Shared Notes Memory]
```

## Key Concepts
- **Specialized Worker Prompts**: Constraining agent personas to single responsibilities prevents hallucination and context pollution.
- **Shared Working Memory (`notes.md`)**: Agents read and write to an explicit file-based scratchpad rather than passing sprawling context windows.
- **Token Usage Tracking**: Granular tracking of prompt tokens, completion tokens, and latency across each agent turn.

## Files
- `multi_agent.py`: Multi-agent manager coordinating search and math workers.
- `single_agent.py`: Baseline single-agent comparison implementation.
- `tools.py`: Tool definitions (Tavily search, arithmetic) and token tracking utilities.
- `notes.md`: Shared persistent scratchpad documenting intermediate agent thoughts and tool outputs.

## Running
```bash
cd week5/multiagent

# Run multi-agent orchestrator:
uv run multi_agent.py

# Compare against single agent:
uv run single_agent.py
```
