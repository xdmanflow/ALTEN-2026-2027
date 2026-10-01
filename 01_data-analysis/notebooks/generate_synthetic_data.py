"""Generate a synthetic recruitment dataset for public demos.

No real data is used: every value is randomly generated.
Usage: python generate_synthetic_data.py [n_rows]
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)
OUT = Path(__file__).parent / "synthetic" / "interviews.csv"


def generate(n: int = 500) -> pd.DataFrame:
    start = np.datetime64("2026-01-05")
    interview_date = start + RNG.integers(0, 260, n).astype("timedelta64[D]")

    status = RNG.choice(["done", "scheduled", "cancelled"], n, p=[0.8, 0.1, 0.1])
    score = np.where(status == "done", RNG.integers(1, 6, n), np.nan)

    outcome = np.full(n, "in_progress", dtype=object)
    done = status == "done"
    outcome[done] = RNG.choice(
        ["hired", "rejected", "dropout", "in_progress"], done.sum(), p=[0.2, 0.5, 0.15, 0.15]
    )

    reasons = {
        "rejected": ["Skills", "Experience", "Communication", "Salary"],
        "dropout": ["Other offer", "Salary", "Location", "No response"],
    }
    outcome_reason = [RNG.choice(reasons[o]) if o in reasons else None for o in outcome]

    offered = np.isin(outcome, ["hired"]) | (RNG.random(n) < 0.05) & done
    offer_date = np.where(
        offered, interview_date + RNG.integers(2, 30, n).astype("timedelta64[D]"), np.datetime64("NaT")
    )
    acceptance_date = np.where(
        outcome == "hired", offer_date + RNG.integers(1, 15, n).astype("timedelta64[D]"), np.datetime64("NaT")
    )

    return pd.DataFrame(
        {
            "interview_id": [f"INT-{i:04d}" for i in range(n)],
            "candidate_id": [f"CAND-{i:04d}" for i in RNG.permutation(n)],
            "interview_date": interview_date,
            "interview_status": status,
            "division": RNG.choice(["Division A", "Division B", "Division C"], n),
            "department": RNG.choice([f"Dept {i}" for i in range(1, 6)], n),
            "recruiter_team": RNG.choice([f"Team {i}" for i in range(1, 5)], n),
            "score": score,
            "school": RNG.choice([f"School {c}" for c in "ABCDEFGHIJKL"], n),
            "school_group": RNG.choice(["Group A", "Group B", "Group C", "Other"], n, p=[0.25, 0.35, 0.25, 0.15]),
            "skill_family": RNG.choice(["Software", "Data", "Mechanical", "Electronics", "Systems"], n),
            "source": RNG.choice(["Job board", "Referral", "Website", "School partnership", "LinkedIn"], n),
            "desired_location": RNG.choice(["Local", "Regional", "National"], n, p=[0.5, 0.3, 0.2]),
            "offer_date": offer_date,
            "acceptance_date": acceptance_date,
            "outcome": outcome,
            "outcome_reason": outcome_reason,
        }
    )


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    OUT.parent.mkdir(parents=True, exist_ok=True)
    generate(n).to_csv(OUT, index=False)
    print(f"Synthetic dataset written to {OUT} ({n} rows)")
