import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "workspace" / "data" / "pipeline.json"

REQUIRED = {
    "company",
    "role",
    "status",
    "priority",
    "fit_score",
    "employment_model",
    "compensation",
    "location",
    "source",
    "last_contact_date",
    "next_action",
    "deadline",
    "notes",
}

VALID_STATUSES = {
    "found",
    "saved",
    "applied",
    "recruiter-screen",
    "technical-screen",
    "onsite-loop",
    "final-round",
    "offer",
    "accepted",
    "rejected",
    "withdrawn",
    "inactive",
}


def main():
    if not PIPELINE.exists():
        print("Private workspace missing. Run: python3 scripts/init_workspace.py")
        raise SystemExit(1)

    data = json.loads(PIPELINE.read_text(encoding="utf-8"))
    opportunities = data.get("opportunities", [])
    errors = []

    for i, item in enumerate(opportunities):
        missing = REQUIRED - set(item.keys())
        if missing:
            errors.append(f"Opportunity {i} missing fields: {sorted(missing)}")
        status = item.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(f"Opportunity {i} has invalid status: {status}")

    if errors:
        print("Pipeline validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"Pipeline looks valid. Opportunities: {len(opportunities)}")


if __name__ == "__main__":
    main()
