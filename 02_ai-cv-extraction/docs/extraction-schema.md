# Extraction Schema

> Generic fields. Final field list and reference values are aligned with the business team.

| Field | Type | Required | Rule | If not found |
|---|---|---|---|---|
| `first_name` | string | yes | As written in the CV | flag |
| `last_name` | string | yes | As written in the CV | flag |
| `email` | string | no | Valid email format | empty |
| `phone` | string | no | Normalized international format | empty |
| `location` | string | no | City / region as written | empty |
| `education_level` | enum | yes | Highest degree mapped to a reference scale | flag |
| `school` | string | yes | School of the highest degree | flag |
| `school_group` | enum | no | Mapped from a reference list; unknown schools → `other` | `other` |
| `graduation_year` | integer | no | 4-digit year | empty |
| `specialization` | string | no | Field of study as written | empty |
| `skill_family` | enum | yes | Mapped to a reference list of skill families | flag |
| `years_of_experience` | number | no | Computed from dated experiences only | empty |
| `languages` | list | no | Languages **explicitly** listed, with level if given | empty |
| `availability` | string | no | Only if explicitly stated | empty |

## Validation rules

- Every value must be **grounded**: present (or directly derivable) in the CV text.
- Enum fields only accept values from their reference list.
- `languages`: a native language is recorded only if the CV states it explicitly — never inferred from the candidate's name.
- Unknown or ambiguous values → empty + review flag, never a guess.

## Output example (synthetic)

```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "jane.doe@example.com",
  "education_level": "master",
  "school": "Example Engineering School",
  "school_group": "other",
  "specialization": "Embedded systems",
  "skill_family": "electronics",
  "years_of_experience": 2,
  "languages": [{"language": "English", "level": "C1"}],
  "review_flags": ["school_group: school not in reference list"]
}
```
