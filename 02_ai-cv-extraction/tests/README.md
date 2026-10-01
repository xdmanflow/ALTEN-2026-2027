# Tests

All tests use **synthetic CVs** — never real candidate documents.

| Test type | What it checks |
|---|---|
| Unit tests | Each stage in isolation (text extraction, validation, normalization) |
| Schema tests | Outputs always match the extraction schema |
| Grounding tests | No value is returned that is absent from the source text |
| Regression tests | Evaluation scores don't drop after a prompt / model change |

```bash
pytest tests/
```
