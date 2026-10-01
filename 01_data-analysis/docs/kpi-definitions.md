# Recruitment KPI Definitions

> Generic definitions. Exact business rules are agreed with stakeholders before computation.

## Volume

| KPI | Definition | Formula |
|---|---|---|
| Applications | Number of applications over the period | `count(applications)` |
| Interviews | Number of interviews held over the period | `count(interviews where status = done)` |
| Offers | Number of offers made | `count(offers)` |
| Hires | Number of accepted offers | `count(offers where accepted)` |

## Conversion

| KPI | Definition | Formula |
|---|---|---|
| Interview → offer rate | Share of interviews leading to an offer | `offers / interviews` |
| Offer acceptance rate | Share of offers accepted | `hires / offers` |
| Overall conversion rate | Share of applications leading to a hire | `hires / applications` |
| Conversion by source | Hires generated per sourcing channel | `hires(source) / applications(source)` |

## Speed

| KPI | Definition | Formula |
|---|---|---|
| Time to offer | Delay between interview and offer | `median(offer_date − interview_date)` |
| Time to acceptance | Delay between offer and acceptance | `median(acceptance_date − offer_date)` |
| Time to hire | Delay between first interview and signature | `median(signature_date − first_interview_date)` |

## Quality

| KPI | Definition | Formula |
|---|---|---|
| Average evaluation score | Mean interview score | `mean(score)` |
| Score distribution | Number of candidates per score level | `count by score` |
| Score by group | Average score per education group / skill family | `mean(score) group by X` (n ≥ 10) |

## Attrition

| KPI | Definition | Formula |
|---|---|---|
| Rejection rate | Share of candidates rejected | `rejected / interviews` |
| Dropout rate | Share of candidates withdrawing | `dropouts / interviews` |
| Top reasons | Most frequent rejection / dropout reasons | `count by reason, sorted` |
| Cancellation rate | Share of scheduled interviews cancelled | `cancelled / scheduled` |
