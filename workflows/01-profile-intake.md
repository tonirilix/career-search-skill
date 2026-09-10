# Workflow: Profile Intake

## Goal

Build a candidate source of truth that can be reused across role analysis, applications, recruiter replies, interview prep, and offer decisions.

## Inputs

- Resume
- LinkedIn profile or summary
- Target roles
- Compensation expectations
- Location and authorization
- Preferred employment models
- Writing/tone preferences
- Career stories
- Dealbreakers

## Process

1. Read all existing files in `user-profile/`.
2. Identify missing or stale fields.
3. Ask for only the missing information required for the current task.
4. Update the relevant files.
5. Create a concise `candidate snapshot` inside `career-profile.md`.
6. Update `strengths-and-gaps.md` to prevent overclaiming.
7. Update `writing-style.md` with tone preferences observed from the user.

## Output

Updated user profile files.

## Quality checks

- Are all claims defensible?
- Are compensation numbers consistent?
- Are target roles clear?
- Are dealbreakers explicit?
- Does writing style reflect the candidate's actual preferences?
