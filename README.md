# Data Analyst & AI Engineering Intern @ ALTEN

> Tracking repo for my 20-week engineering internship within ALTEN's Recruitment department (Toulouse), combining **recruitment data analysis** and the **design of an AI-powered automation solution**.

> ⚠️ **Confidentiality:** this repository contains **no company data, no candidate information, and no internal documents**. Only material explicitly authorized by ALTEN (sanitized, anonymized, or synthetic) is published here.

---

## Table of Contents

- [About the Internship](#about-the-internship)
- [Missions](#missions)
- [Tech Stack](#tech-stack)
- [Skills Developed](#skills-developed)
- [Timeline](#timeline)
- [Repo Structure](#repo-structure)
- [Internship Report & Defense](#internship-report--defense)
- [Progress Tracker](#progress-tracker)
- [Confidentiality & License](#confidentiality--license)

---

## About the Internship

| Item | Details |
|---|---|
| Company | ALTEN France (Engineering & IT consulting) |
| Location | Toulouse, France |
| Department | Recruitment |
| Role | Data Analyst & AI Engineering Intern |
| Duration | 20 weeks — September 14, 2026 → January 29, 2027 |
| Academic context | CESI École d'Ingénieurs — Engineering degree, Computer Science (AI & Data Science track) |

The internship sits at the intersection of **data** and **AI** applied to recruitment: turning recruitment activity data into actionable insights for decision-makers, and reducing repetitive manual work through AI-driven automation.

---

## Missions

### 1. Recruitment Data Analysis — *Data Analyst*

Turn raw recruitment data into **actionable insights** for stakeholders.

- Collect, clean and structure data exported from recruitment tools (tidy data principles)
- Define and compute recruitment KPIs (activity, candidate quality, conversion, time-to-offer, sourcing efficiency)
- Build dashboards and visuals answering concrete business questions
- Document the data processing methodology

**Planned dashboard structure:**

| Page | Business question | Examples of visuals |
|---|---|---|
| Overview | Where do we stand? | KPI cards (volumes, conversion rate, median time-to-offer) |
| Activity | How much are we interviewing? | Weekly trends, breakdown by team/division, interview status |
| Quality | How strong are the candidates? | Score distributions, averages by education and skill family |
| Funnel | How do interviews turn into hires? | Conversion funnel, lead times, main rejection/dropout reasons |
| Hires | Where do our hires come from? | Hires by education, skills, division, location, sourcing channel |

### 2. AI-Powered CV Information Extraction — *AI Engineer*

Design and build a solution that **automatically extracts key information from CVs** to pre-fill candidate profiles in the recruitment platform (ATS), replacing a slow and repetitive manual process.

- Document processing (PDF CVs → structured data)
- LLM-based information extraction with a defined output schema
- Data validation and handling of ambiguous / missing information
- Evaluation protocol to measure extraction accuracy and limit errors
- Focus on reliability, security and compliance (personal data)

### 3. Operational Support

- Structuring candidate data from CVs into the recruitment platform — hands-on work that provided the domain knowledge and edge cases used to design the automation (Mission 2)
- Ad-hoc data analyses for recruitment teams

### 4. Candidate–Job Matching — *Exploratory*

Potential extension: matching candidate profiles with open positions. Scope to be defined.

---

## Tech Stack

| Area | Tools |
|---|---|
| Data cleaning & analysis | Excel, Python (pandas), SQL |
| Visualization & reporting | Dashboards, Python visualization libraries |
| AI / LLM engineering | Python, LLM APIs, document (PDF) processing |
| Quality | Data validation, testing, evaluation metrics |
| Workflow | Git / GitHub, AI-assisted development |

---

## Skills Developed

| Domain | Skills targeted | Status |
|---|---|---|
| Data cleaning | Tidy data, normalization, deduplication, missing values | 🟡 In progress |
| Recruitment KPIs | Funnel metrics, conversion rate, time-to-offer, sourcing efficiency | 🟡 In progress |
| Data visualization | Dashboard design, storytelling for stakeholders | 🟡 In progress |
| Python & testing | Clean code, unit tests, project structure | 🟡 In progress |
| APIs & web | Consuming APIs, authentication, error handling | ⚪ To do |
| LLM engineering | Prompt design, structured outputs, extraction pipelines | 🟡 In progress |
| Evaluation | Ground truth datasets, accuracy metrics, error analysis | ⚪ To do |
| Data validation | Schemas, consistency checks | ⚪ To do |
| Backend & deployment | Serving a solution, packaging, environments | ⚪ To do |
| Security & compliance | Personal data handling (GDPR), secrets management | ⚪ To do |
| Engineering judgement | Trade-offs, scoping, communicating with stakeholders | 🟡 In progress |

---

## Timeline

| Phase | Period | Focus |
|---|---|---|
| 1. Onboarding | Weeks 1–2 | Company & recruitment process discovery, tools, operational support |
| 2. Launch | Weeks 3–6 | Data cleaning & first analyses · AI solution design and prototyping |
| 3. Build | Weeks 7–14 | Dashboards delivery · Extraction pipeline development & evaluation |
| 4. Consolidation | Weeks 15–17 | Testing, documentation, handover |
| 5. Wrap-up | Weeks 18–20 | Internship report & defense preparation |

---

## Repo Structure

```
ALTEN-2026/
├── 01_data-analysis/
│   ├── docs/                  # Methodology, KPI definitions, data dictionary (generic)
│   ├── notebooks/             # Analysis notebooks — synthetic/anonymized data only
│   └── visuals/               # Authorized, anonymized dashboard screenshots
│
├── 02_ai-cv-extraction/
│   ├── docs/                  # Architecture, extraction schema, evaluation protocol
│   ├── src/                   # Source code (only if authorized)
│   └── tests/                 # Tests on synthetic CVs
│
├── 03_candidate-matching/     # Exploratory work (if the project starts)
│
├── 04_learning/               # Personal notes on skills learned during the internship
│
├── 05_internship-report/
│   ├── outline.md             # Report plan
│   ├── drafts/                # Working drafts
│   └── final/                 # Final version (validated by ALTEN)
│
├── 06_defense/
│   ├── slides/                # Defense presentation (.pptx / .pdf)
│   └── speaker-notes.md       # Talking points & Q&A preparation
│
├── .gitignore                 # Excludes any real data / credentials
├── LICENSE
└── README.md
```

---

## Internship Report & Defense

**Internship report** (`05_internship-report/`) — written at the end of the internship (December–January), validated by ALTEN before publication.

- [ ] Report outline
- [ ] Company & context presentation
- [ ] Mission 1 — Data analysis: approach, results, impact
- [ ] Mission 2 — AI solution: design, implementation, evaluation
- [ ] Skills acquired & critical analysis
- [ ] Conclusion & perspectives
- [ ] Validation by company tutor
- [ ] Final version submitted

**Defense** (`06_defense/`) — presentation summarizing the internship for the academic jury.

- [ ] Slide deck structure
- [ ] Slides (context, missions, results, skills, conclusion)
- [ ] Speaker notes
- [ ] Rehearsal & Q&A preparation

---

## Progress Tracker

- [x] **Phase 1 — Onboarding** (weeks 1–2)
- [ ] **Phase 2 — Launch** (weeks 3–6)
  - [x] First data cleaning completed
  - [ ] First set of dashboards delivered
  - [ ] AI solution design validated
- [ ] **Phase 3 — Build** (weeks 7–14)
- [ ] **Phase 4 — Consolidation** (weeks 15–17)
- [ ] **Phase 5 — Wrap-up** (weeks 18–20)

---

## Confidentiality & License

All data, documents and internal information related to ALTEN, its candidates, clients and employees remain confidential and are **not** published in this repository. Any content shared here has been authorized by ALTEN and is sanitized, anonymized or synthetic.

Copyright © 2026 ALTEN. All rights reserved.

This software is proprietary and confidential. Unauthorized copying, distribution, modification, or use of this software, in whole or in part, is strictly prohibited without prior written consent from ALTEN.
