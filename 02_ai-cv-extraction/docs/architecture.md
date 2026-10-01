# Architecture

## 1. Pipeline stages

| # | Stage | Role | Key concerns |
|---|---|---|---|
| 1 | **Ingestion** | Receive the CV file | Supported formats, file size, encoding |
| 2 | **Text extraction** | PDF → raw text (OCR fallback for scanned CVs) | Multi-column layouts, tables, scanned documents |
| 3 | **Preprocessing** | Clean and normalize text | Noise removal, language detection |
| 4 | **LLM extraction** | Raw text → structured JSON following the [schema](extraction-schema.md) | Prompt design, structured output, temperature 0 |
| 5 | **Validation** | Check types, allowed values, consistency | Schema validation, reference lists |
| 6 | **Grounding check** | Verify each extracted value appears in the source text | Hallucination detection |
| 7 | **Review routing** | Low-confidence / missing fields flagged for a human | Human in the loop |
| 8 | **Output** | Pre-filled profile ready for the ATS | Integration method to be validated |

## 2. Design principles

- **Human in the loop** — the system proposes, a recruiter validates.
- **No hallucination tolerated** — a value that cannot be found in the CV is left empty and flagged, never guessed.
- **No inference of sensitive attributes** — information not explicitly written in the CV (e.g. native language, origin) is never deduced from a name or photo.
- **Deterministic & traceable** — fixed prompts, versioned, low temperature; every output links back to its source text.
- **Privacy by design** — personal data processed only through approved services, nothing stored longer than necessary, no data in logs.

## 3. Design decisions log

| Date | Decision | Alternatives considered | Rationale |
|---|---|---|---|
| | | | |

## 4. Open questions

- [ ] Integration method with the ATS (manual copy, export, API)
- [ ] Hosting constraints (approved services, data residency)
- [ ] Handling of CVs in languages other than French / English
