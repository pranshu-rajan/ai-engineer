# Day 6: Prompt Engineering in Practice

## Overview
Comparative study of prompt design patterns: analyzing bad/vague prompts vs. well-structured, production-grade prompts with clear roles, constraints, context, and explicit output formats.

## Key Concepts
- **Prompt Structure**: `#ROLE`, `#CONTEXT`, `#TASK`, and `#CONSTRAINTS`.
- **Few-Shot Prompting**: Providing representative input-output pairs to guide tone and format.
- **Guardrails against Hallucinations**: Constraining answers strictly to provided context.

## Files
- `prompt_eng.py`: Compares raw unstructured prompts vs. well-framed enterprise support prompts.
- `main.py`: Entry point.

## Running
```bash
uv run prompt_eng.py
```
