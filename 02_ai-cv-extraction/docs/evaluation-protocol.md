# Evaluation Protocol

## 1. Goal

Measure extraction quality objectively before any deployment, and compare candidate approaches (models, prompts, text extraction methods) on the same basis.

## 2. Evaluation dataset

- **Synthetic or anonymized CVs only**, covering diverse layouts (one/two columns, tables, scanned, FR/EN).
- Each CV annotated by hand with the expected value of every field (**ground truth**).
- Dataset split kept fixed so results stay comparable over time.

| Category | Target number of CVs |
|---|---|
| Standard layout | |
| Multi-column / design-heavy | |
| Scanned (OCR) | |
| English-language | |
| Edge cases (missing info, unusual schools…) | |

## 3. Metrics

| Metric | Definition | Target |
|---|---|---|
| Field accuracy | % of fields whose value matches ground truth (after normalization) | TBD |
| Exact match rate | % of CVs with **all** required fields correct | TBD |
| Hallucination rate | % of extracted values not present in the source CV | **≈ 0** |
| Missing rate | % of fields left empty while present in the CV | TBD |
| Flag precision | % of review flags that were justified | TBD |
| List F1 | Precision / recall on list fields (languages, skills) | TBD |
| Latency & cost | Time and cost per CV | TBD |

## 4. Comparison template

| Approach | Field accuracy | Hallucination rate | Missing rate | Latency | Notes |
|---|---|---|---|---|---|
| Approach A | | | | | |
| Approach B | | | | | |

## 5. Error analysis

For each error: field, CV category, error type (*wrong value / hallucination / missing / format*), probable cause, fix.

| CV | Field | Expected | Got | Error type | Cause | Fix |
|---|---|---|---|---|---|---|
| | | | | | | |
