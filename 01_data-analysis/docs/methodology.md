# Data Processing Methodology

## 1. Principles

Cleaning follows the **tidy data** principles (H. Wickham, 2014):

- each **variable** is a column
- each **observation** is a row
- each **type of observational unit** is a table

## 2. Pipeline

```mermaid
flowchart LR
    A[Raw export] --> B[Profiling]
    B --> C[Cleaning]
    C --> D[Validation]
    D --> E[Analysis]
    E --> F[Dashboards]
    F --> G[Insights & recommendations]
```

## 3. Cleaning checklist

### Structure
- [ ] Remove empty rows / columns and export artefacts (merged headers, totals)
- [ ] One header row, consistent column names (`snake_case`, no accents)
- [ ] Split multi-value columns into separate variables or rows

### Types & formats
- [ ] Dates parsed into a single format (ISO 8601: `YYYY-MM-DD`)
- [ ] Numeric fields stored as numbers (scores, durations)
- [ ] Categorical values normalized (case, spelling variants, trailing spaces)

### Quality
- [ ] Duplicates identified and handled (rule documented)
- [ ] Missing values quantified per column; strategy documented (keep / impute / exclude)
- [ ] Outliers checked (e.g. negative durations, impossible dates)
- [ ] Consistency checks across columns (e.g. offer date ≥ interview date)

### Traceability
- [ ] Every transformation documented (what, why, impact on row count)
- [ ] Raw data kept untouched; cleaning is reproducible

## 4. Cleaning log template

| Step | Transformation | Reason | Rows before | Rows after |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## 5. Analysis rules

- Minimum sample size before comparing groups (e.g. **≥ 10 observations** per category)
- Medians preferred over means for durations (skewed distributions)
- Every chart answers one explicit business question
- Every insight states its limits (sample size, missing data, period covered)

## References

- Wickham, H. (2014). *Tidy Data*. Journal of Statistical Software, 59(10).
