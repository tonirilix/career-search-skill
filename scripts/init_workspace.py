from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIRS = [
    "data/jobs/raw",
    "data/jobs/analyzed",
    "data/jobs/rejected",
    "data/companies",
    "outputs/drafts",
    "outputs/application-packets",
    "outputs/interview-prep",
    "outputs/reports",
]

for rel in DIRS:
    path = ROOT / rel
    path.mkdir(parents=True, exist_ok=True)
    keep = path / ".gitkeep"
    if not keep.exists():
        keep.write_text("", encoding="utf-8")

print("Workspace folders are ready.")
