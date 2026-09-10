# Workflow: Fit Analysis

## Goal

Assess whether a role is worth pursuing and how the candidate should position themselves.

## Inputs

- Normalized role file
- Candidate profile
- Preferences
- Compensation profile
- Strengths and gaps

## Scoring rubric

Score each category from 0 to 5.

| Category | Weight | Meaning |
|---|---:|---|
| Location/work authorization | 15 | Can the company realistically hire/contract the candidate? |
| Employment model | 10 | Full-time/contractor/EOR alignment |
| Stack fit | 20 | Match with strongest technical skills |
| Seniority/scope | 15 | Scope aligns with current/proposed level |
| Product/domain fit | 10 | Product complexity and interest |
| Compensation likelihood | 10 | Expected comp matches target |
| Growth potential | 10 | Good next step for career direction |
| Company quality/risk | 10 | Stability, culture, red flags |

Total: 100.

## Fit labels

- 85-100: Strong match
- 70-84: Good match
- 55-69: Possible match
- 40-54: Stretch / low priority
- below 40: Reject unless strategic reason

## Required output

Use `templates/fit-analysis.md`.

Include:

- score
- verdict
- why it fits
- risks/gaps
- how to position the candidate
- what not to overclaim
- compensation/employment notes
- recommended next action

## Important judgment rule

Do not let a high stack match hide major red flags such as location incompatibility, weekend expectations, unclear contractor terms, or unrealistic compensation.
