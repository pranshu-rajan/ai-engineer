# Week 6 Capstone: Autonomous Coding & Bug-Fixing Agent

## Overview
An autonomous software engineering agent that diagnoses and repairs bugs in codebases directly from plain English problem descriptions. The agent navigates repository files, locates erroneous code, applies surgical edits, compiles and validates with `g++`, and rolls back changes automatically if unsuccessful within a retry budget.

## Agent Loop & Workflow
```
[User Bug Description]
         |
         v
[LLM Tool Execution Loop]
   1. search_files()      -> Discover candidate files
   2. search_in_file()    -> Pinpoint relevant line numbers
   3. replace_line()      -> Apply surgical code patch
         |
         v
[Compilation & Execution Check]
   - Compile via g++ (subprocess)
   - If compile fails: auto-retry with error feedback (up to 3 attempts)
   - If compile passes: verify behavior with user
   - If 3 attempts exhausted: automatic rollback to pristine state
```

## Tech Stack
- **Groq API**: `openai/gpt-oss-120b` for reasoning and tool generation.
- **Subprocess & Compilers**: Direct system-level execution and testing.
- **Atomic Rollback**: Workspace snapshotting to guarantee no broken code remains on failure.

## Files
- `main.py`: Core agent loop, compiler execution harness, and state management.
- `tools.py`: File inspection and surgical replacement tools (`search_files`, `search_in_file`, `replace_line`).
- `cpp_project/main.cpp`: Test C++ project used for bug injection and automated repair benchmarks.
- `prompt.md`: Agent specifications and architectural constraints.

## Running
```bash
cd week6/codingagent

# Launch agent against sample C++ project:
uv run main.py
```
