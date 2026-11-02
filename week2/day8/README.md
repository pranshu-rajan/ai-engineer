# Day 8: LLM Chaining Pipelines

## Overview
Decomposing complex multi-stage reasoning tasks into deterministic sequential LLM chains. Instead of asking one massive prompt to do everything, the pipeline feeds the output of step N into step N+1.

## Key Concepts
- **Sequential Chains**:
  - Stage 1: Analyze Job Description (extract hard skills, soft skills, seniority).
  - Stage 2: Analyze Candidate Resume against the extracted criteria.
  - Stage 3: Match scoring, skill gap identification, and personalized recommendation generation.
- **Error Propagation Mitigation**: Formatting intermediate outputs to prevent downstream degradation.

## Files
- `chain.py`: Multi-step JD & Resume matching chain pipeline.
- `main.py`: Entry point.

## Running
```bash
uv run chain.py
```
