# Day 5: Capstone Project — Resume Parser

## Overview
A real-world extraction pipeline that reads multi-format resumes (PDF, DOCX) and parses them into a standardized, strongly-typed JSON schema using Pydantic and Groq's LLM API.

## Architecture
1. **Document Ingestion**: Reads `.pdf` via `pypdf` and `.docx` via `python-docx`.
2. **Text Normalization**: Extracts raw text blocks and strips non-printable whitespace.
3. **Structured Extraction**: Prompts the LLM with the Pydantic JSON schema to extract:
   - Candidate Contact (Name, Email, Phone, Links)
   - Total Work Experience (Years calculated)
   - Work History (Company, Role, Duration, Responsibilities, Technologies used)
   - Education & Certifications
   - Skills matrix
4. **Validation**: Pydantic validates data types and fills optional defaults cleanly.

## Files
- `resume_parser.py`: Core resume parsing engine.
- `resumes/`: Test dataset containing sample resumes in PDF and DOCX formats.
- `main.py`: CLI harness for running batch parsing across test resumes.

## Running
```bash
uv run resume_parser.py
```
