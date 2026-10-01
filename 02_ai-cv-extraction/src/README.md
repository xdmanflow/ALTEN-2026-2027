# Source Code

> Code is published here **only with explicit authorization** from ALTEN. Until then, this folder documents the planned structure.

```
src/
├── ingestion.py        # File loading & format checks
├── text_extraction.py  # PDF → text (+ OCR fallback)
├── extraction.py       # LLM call with structured output
├── schema.py           # Output schema & validation rules
├── grounding.py        # Checks values against source text
├── pipeline.py         # Orchestrates all stages
└── config.py           # Settings (no secrets — loaded from environment)
```

Secrets (API keys) are **never** committed — they are read from environment variables (`.env` is git-ignored).
