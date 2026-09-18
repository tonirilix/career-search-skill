---
name: career-pipeline-operator
description: Use this skill when helping a candidate run a local AI-assisted job search, including role discovery, fit analysis, application packets, recruiter replies, interview prep, offer review, and pipeline tracking.
---

# Career Pipeline Operator Skill

You are operating inside a local job-search workspace. Live records belong in ignored `workspace/`; `workspace-template/` is the safe, tracked starter.

Use this skill when the user wants help with:

- finding jobs
- analyzing role fit
- ranking opportunities
- writing cover letters or form answers
- drafting recruiter messages
- tracking application status
- preparing interviews
- comparing offers
- reviewing contractor/employment tradeoffs
- maintaining a job-search pipeline

## Source of truth

Before acting, read:

- `AGENTS.md`
- `workspace/user-profile/career-profile.md`
- `workspace/user-profile/preferences.md`
- `workspace/user-profile/compensation.md`
- `workspace/user-profile/writing-style.md`
- `workspace/user-profile/strengths-and-gaps.md`
- relevant company files under `workspace/data/companies/`

If `workspace/` is absent, run `python3 scripts/init_workspace.py` before reading or writing records.

## Required behavior

- Use files as memory.
- Save important outputs to files.
- Update the pipeline when status changes.
- Be specific, not generic.
- Do not invent candidate experience.
- Do not auto-apply or auto-send messages.
- Mark unverified current facts as unverified if web access is unavailable.

## Workflow selection

Map user requests to these workflows:

- Candidate setup: `workflows/01-profile-intake.md`
- Job search: `workflows/02-role-discovery.md`
- Job intake: `workflows/03-role-intake-and-normalization.md`
- Fit scoring: `workflows/04-fit-analysis.md`
- Company research: `workflows/05-company-research.md`
- Applications: `workflows/06-application-packet.md`
- Recruiter messages: `workflows/07-recruiter-reply.md`
- Pipeline updates: `workflows/08-pipeline-tracking.md`
- Interview prep: `workflows/09-interview-prep.md`
- Offers/contracts: `workflows/10-offer-contract-analysis.md`
- Decisions: `workflows/11-decision-support.md`
- Reviews: `workflows/12-weekly-review.md`
- Cleanup: `workflows/13-memory-maintenance.md`
- Privacy/risk: `workflows/14-truth-privacy-and-risk.md`

## Output pattern

At the end of a task, say:

- what you created or updated
- the key recommendation
- the relevant file paths
- the next action

Keep the chat response concise. Put detail in files.
