# Workflow: Memory Maintenance

## Goal

Keep the workspace accurate as the job search evolves.

## Trigger

Run when:

- the user says memory feels stale
- a process changes significantly
- an offer is accepted/rejected
- compensation expectations change
- candidate profile changes
- weekly review finds contradictions

## Checks

- Is `pipeline.json` current?
- Are closed roles marked inactive/rejected/withdrawn?
- Are deadlines accurate?
- Are compensation numbers consistent?
- Are company folders complete?
- Are stale assumptions marked or removed?
- Are drafts saved in the correct locations?
- Are role analyses based on current postings?

## Output

- Update files directly.
- Create `workspace/outputs/reports/memory-maintenance-<date>.md` summarizing changes.

## Rule

Do not silently delete important history. Archive or mark stale instead.
