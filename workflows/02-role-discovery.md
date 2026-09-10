# Workflow: Role Discovery

## Goal

Find jobs that are actually worth the candidate's time.

## Inputs

- Candidate preferences
- Target titles
- Location constraints
- Stack preferences
- Compensation expectations
- Target companies
- Known dealbreakers

## Search strategy

If web access is available, search using combinations of:

- target titles
- stack terms
- remote country/location terms
- company type preferences
- seniority terms
- domain terms
- AI-related terms if relevant

## Query generation rule

Do not use hardcoded searches. Build queries from `user-profile/preferences.md`, `user-profile/career-profile.md`, and `user-profile/strengths-and-gaps.md`.

Example format:

```text
[Target title] [primary skill] [secondary skill] remote [candidate country/region] [company preference]
[Target title] [domain preference] [seniority] [remote/location constraint]
```

## Discovery rules

For every found role, verify or mark as unknown:

- Is it still open?
- Is remote work allowed from candidate location?
- Is the employment model clear?
- Is the stack aligned?
- Is the seniority aligned?
- Is compensation available or inferable?
- Is the company product, consultancy, agency, or unclear?
- Are there red flags?

## Output

Create raw discovery notes:

```text
data/jobs/raw/<date>-role-discovery.md
```

Create analyzed job files for promising roles:

```text
data/jobs/analyzed/<company>-<role>.md
```

Update:

```text
data/role-shortlist.json
```

## Ranking buckets

Use these buckets:

- Strong match
- Good match
- Possible match
- Stretch
- Low priority
- Reject

## Do not recommend

- closed jobs unless user asks about history
- jobs with incompatible location requirements
- jobs below minimum compensation unless there is a strategic reason
- jobs requiring skills far outside the candidate profile without clear ramp path
