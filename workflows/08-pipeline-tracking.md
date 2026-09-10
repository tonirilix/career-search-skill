# Workflow: Pipeline Tracking

## Goal

Keep an accurate local CRM for the candidate's job search.

## Files

- `data/pipeline.json`
- `data/next-actions.md`
- `data/companies/<company>/process.md`

## When to update

Update the pipeline whenever:

- a role is found or saved
- an application is submitted
- a recruiter responds
- an interview is scheduled
- interview feedback arrives
- compensation is discussed
- an offer is received
- a process is rejected/withdrawn/accepted
- a deadline changes

## Required fields in `pipeline.json`

- company
- role
- status
- priority
- fit_score
- employment_model
- compensation
- location
- source
- last_contact_date
- next_action
- deadline
- notes

## Company process file sections

Use `templates/company-process.md`.

Include:

- current status
- timeline
- key contacts
- role summary
- compensation discussed
- interview stages
- pending questions
- risks
- recommended next action

## Priority levels

- P1: actively prioritize
- P2: good but secondary
- P3: low priority/watch
- P4: reject/inactive

## Next action quality

A next action should be concrete:

Bad:

`Follow up.`

Good:

`Send PTO clarification question before signing contractor agreement.`
