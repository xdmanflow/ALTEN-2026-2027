# Candidate–Job Matching — *Exploratory*

> Potential extension: matching candidate profiles with open positions. **Scope to be defined.**

## Idea

Given a set of candidate profiles and a set of open positions, rank the most relevant candidates for each position (and vice versa).

## Possible approaches (to be evaluated)

| Approach | Principle | Pros | Cons |
|---|---|---|---|
| Rule-based | Weighted matching on structured fields (skills, level, location) | Transparent, simple | Rigid, needs clean data |
| Semantic similarity | Embeddings of profiles and job descriptions | Handles synonyms and free text | Less explainable |
| Hybrid | Hard filters + semantic ranking | Best of both | More complex |

## Requirements before starting

- [ ] Business need and success criteria defined
- [ ] Data sources and access validated
- [ ] Fairness review: matching must not rely on sensitive or proxy attributes
- [ ] Human validation of every recommendation

## Status

Not started
