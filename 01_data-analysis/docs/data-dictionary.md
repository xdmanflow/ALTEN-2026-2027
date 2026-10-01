# Data Dictionary (generic)

> Generic field descriptions used for the analysis. Field names are illustrative and do **not** reflect internal systems.

| Field | Type | Description | Example values |
|---|---|---|---|
| `interview_id` | string | Unique interview identifier (anonymized) | `INT-0001` |
| `candidate_id` | string | Unique candidate identifier (anonymized) | `CAND-0001` |
| `interview_date` | date | Date of the interview | `2026-09-15` |
| `interview_status` | category | Interview status | `done`, `scheduled`, `cancelled` |
| `division` | category | Business division | `Division A` |
| `department` | category | Department | `Dept 1` |
| `recruiter_team` | category | Team in charge (anonymized) | `Team 1` |
| `score` | integer | Interview evaluation score | `1` – `5` |
| `school` | category | School / university | `School X` |
| `school_group` | category | School category | `Group A`, `Group B`, `Other` |
| `skill_family` | category | Main skill family | `Software`, `Mechanical`, `Data` |
| `source` | category | Sourcing channel | `Job board`, `Referral`, `Website` |
| `desired_location` | category | Desired work location / mobility | `Toulouse`, `National` |
| `offer_date` | date | Date of offer (if any) | `2026-09-25` |
| `acceptance_date` | date | Date of acceptance (if any) | `2026-09-30` |
| `outcome` | category | Final outcome | `hired`, `rejected`, `dropout`, `in_progress` |
| `outcome_reason` | category | Rejection / dropout reason | `Salary`, `Other offer`, `Skills` |
