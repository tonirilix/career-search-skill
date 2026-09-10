import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "data" / "companies" / "_template"
COMPANIES_DIR = ROOT / "data" / "companies"


def slugify(value: str) -> str:
    return "-".join(value.lower().strip().replace("_", "-").split())


def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/add_company.py <company> [role title]')
        raise SystemExit(1)

    company = sys.argv[1]
    role = sys.argv[2] if len(sys.argv) > 2 else ""
    slug = slugify(company)
    target = COMPANIES_DIR / slug
    target.mkdir(parents=True, exist_ok=True)

    files = ["process.md", "role.md", "recruiter-messages.md", "interviews.md", "offer.md", "notes.md"]
    for name in files:
        src = TEMPLATE_DIR / name
        dst = target / name
        if not dst.exists():
            text = src.read_text(encoding="utf-8") if src.exists() else f"# {name}\n"
            text = text.replace("<Company>", company).replace("<Role>", role).replace("<Role Title>", role)
            if name == "process.md":
                text += f"\n\nCreated: {date.today().isoformat()}\n"
            dst.write_text(text, encoding="utf-8")

    print(f"Created/updated company folder: {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
