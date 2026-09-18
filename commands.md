# Commands

These are command-style prompts the user can give the agent. They are not magical shell commands unless your agent tool implements them. Treat them as workflow triggers.

## Profile

### `/profile-intake`

Goal: fill or refine the candidate source of truth.

Agent should:

1. Read `workflows/01-profile-intake.md`.
2. Inspect `workspace/user-profile/`.
3. Ask for missing resume/preferences/context.
4. Update profile files.
5. Summarize assumptions and missing data.

### `/update-profile`

Use when the user gives new career, compensation, writing style, or preference information.

## Jobs

### `/discover-roles`

Goal: find promising roles based on the profile.

Agent should:

1. Read candidate profile and preferences.
2. Build search queries from the profile.
3. Search if web access is available.
4. Save raw findings to `workspace/data/jobs/raw/`.
5. Create analyzed files for promising roles.
6. Update `workspace/data/role-shortlist.json`.

### `/analyze-role`

Use when the user gives a job URL or pasted JD.

Input format:

```text
/analyze-role
Company: <company>
Role: <role>
URL: <url>
Job description: <text>
Notes: <optional>
```

Agent should:

1. Normalize the role.
2. Save the role file.
3. Run fit analysis.
4. Update company and pipeline records.
5. Recommend next action.

## Applications

### `/create-application-packet <company>`

Creates:

- cover letter
- form answers
- positioning notes
- salary answer if needed
- application checklist

Output path:

```text
workspace/outputs/application-packets/<company>/
```

### `/tailor-resume <company>`

Creates role-specific resume tailoring notes. Do not fabricate experience.

## Communication

### `/draft-reply <company>`

Use when the user pastes a recruiter message.

Agent should:

1. Identify the situation.
2. Read company process history.
3. Draft 1-3 response options if tone is delicate.
4. Save the chosen draft if user approves.

### `/follow-up <company>`

Draft a follow-up based on last contact date and stage.

## Interview

### `/prepare-interview <company> <stage>`

Creates stage-specific prep.

Examples:

```text
/prepare-interview <company> recruiter screen
/prepare-interview <company> technical screen
/prepare-interview <company> behavioral interview
/prepare-interview <company> system design
/prepare-interview <company> final culture interview
```

### `/mock-interview <company> <stage>`

Run a simulated interview. Ask one question at a time and provide feedback.

## Offers

### `/analyze-offer <company>`

Analyze compensation, benefits, contractor/full-time implications, risks, and clarification questions.

### `/compare-offers`

Compare active offers and late-stage processes.

## Pipeline

### `/update-status <company> <status>`

Update pipeline and process files.

Allowed statuses:

- found
- saved
- applied
- recruiter-screen
- technical
- onsite-loop
- final
- offer
- accepted
- rejected
- withdrawn
- archived

### `/weekly-review`

Create a weekly review and recommended focus list.
