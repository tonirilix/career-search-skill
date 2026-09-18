# Workflow: Role Intake and Normalization

## Goal

Convert a pasted job description or URL into a durable role record.

## Inputs

- Job URL or pasted job description
- Company name
- Role title
- Location
- Employment model
- User-provided notes

## Output path

```text
workspace/data/jobs/analyzed/<company>-<role>.md
```

Also create or update:

```text
workspace/data/companies/<company>/role.md
workspace/data/companies/<company>/process.md
```

## Normalized fields

- Company:
- Role:
- URL:
- Location:
- Remote eligibility:
- Employment type:
- Seniority:
- Compensation:
- Stack:
- Responsibilities:
- Requirements:
- Nice-to-haves:
- Interview process:
- Recruiter / contact:
- Date found:
- Last verified:
- Status:

## Analysis fields

- Fit verdict:
- Fit score:
- Main alignment points:
- Main gaps:
- Red flags:
- Unknowns:
- Recommended next action:

## Rules

- Preserve original wording for critical requirements.
- Do not infer open status unless verified.
- If web access is unavailable, mark URL/status as unverified.
- If compensation is not listed, do not invent it. You may estimate only if the user asks and the estimate is labeled as inference.
