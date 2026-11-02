# Day 4: Structured Output with Pydantic

## Overview
Moving beyond raw text generation to production-grade reliable outputs. Using Pydantic models to enforce JSON Schema validation and type safety directly from LLM completions.

## Key Concepts
- **JSON Mode & Schema Enforcement**: Guaranteeing model outputs match typed schemas.
- **Pydantic Validation**: Automatic parsing and type coercion into Python classes (`BaseModel`).
- **Data Extraction**: Extracting structured entities, dates, categories, and attributes from unstructured conversational text.

## Files
- `json_pydantic.py`: Pydantic schema definition, schema injection, and JSON validation pipeline.
- `main.py`: Entry point.

## Running
```bash
uv run json_pydantic.py
```
