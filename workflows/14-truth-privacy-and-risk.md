# Workflow: Truth, Privacy, and Risk

## Goal

Protect candidate trust and avoid harmful automation.

## Truth rules

- Do not invent qualifications.
- Do not fabricate employment history.
- Do not claim an application was submitted unless user confirms it.
- Do not say a job is open unless verified or source-provided.
- Do not treat recruiter statements as contract terms unless confirmed in the contract.
- Do not give legal/tax advice as certainty.

## Privacy rules

- Write live records only under the gitignored `workspace/` directory. `workspace-template/` is a public-safe starter, not working memory.
- Keep sensitive data local by default.
- Do not expose references, compensation history, contracts, or recruiter messages externally without approval.
- Redact personal contact data from examples unless needed.
- Do not send emails, submit forms, or upload documents without explicit approval.

Before publishing changes, review staged files and confirm `workspace/` is ignored. See `PRIVACY.md` for the full checklist.

## Risk labels

Use:

- `confirmed`
- `user-provided`
- `recruiter-provided`
- `contract-stated`
- `web-verified`
- `inferred`
- `unverified`
- `requires professional review`

## When to ask before proceeding

Ask a clarifying question when:

- compensation response could commit the candidate to a number
- a draft reveals competing offers
- legal/tax interpretation is central
- the role requires a skill not in the candidate profile
- the user has not approved final wording for sensitive messages

## High-risk tasks

For these tasks, be extra careful:

- contract review
- tax setup
- visa/work authorization
- salary negotiation
- reference sharing
- background checks
- withdrawing from active processes
- accepting offers
