import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "workspace-template"
WORKSPACE = ROOT / "workspace"

if WORKSPACE.exists():
    print("Private workspace already exists; no files were overwritten.")
else:
    shutil.copytree(TEMPLATE, WORKSPACE)
    print("Private workspace created at workspace/ (gitignored).")
