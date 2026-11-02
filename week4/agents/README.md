# Week 4: Tool-Augmented Agents

## Overview
Implementation of autonomous tool-calling agents. Integrates web search (`TavilyClient`), safe expression evaluation, and external APIs with an LLM reasoning engine to solve questions requiring real-time external data.

## Key Concepts
- **Tool Definitions & Schemas**: Declarative JSON schemas telling the LLM when and how to call tools.
- **Function Dispatching**: Intercepting `tool_calls` in the response, executing local Python functions, and feeding structured responses back.
- **Multi-Turn Convergence**: Iterating until the agent decides no further tools are needed and formulates a final response.

## Files
- `myagent.py`: Agent with Tavily web search and math calculator tools using Groq.
- `claude_agent.py`: Agent implementation using Anthropic Claude models.
- `main.py`: Entry point.

## Running
```bash
uv run myagent.py
```
