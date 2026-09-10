# Job Search Operator Skill

A local, file-based agent workspace for running an AI-assisted job search from discovery to signed offer.

This project is designed to work with agentic coding tools such as Claude Code, Codex, Cursor agents, or any assistant that can read and write local files. It is intentionally not a full app. It is a practical bridge between a chat-only workflow and a future product.

The core idea is simple:

- Keep the candidate profile, job pipeline, role analyses, drafts, interview prep, and offer notes as local files.
- Give the agent strict workflows and templates so it behaves like a persistent job-search operator.
- Preserve judgment, personalization, and continuity without requiring one giant chat thread.

## What this skill helps with

- Build and maintain a candidate source of truth.
- Discover or ingest roles.
- Analyze job fit with a consistent rubric.
- Rank opportunities based on the candidate profile and preferences.
- Generate application packets.
- Draft recruiter responses.
- Track each company process.
- Prepare for interviews using role, company, and candidate context.
- Review offers and contractor/full-time tradeoffs.
- Keep a weekly review and next-action queue.

## Quick start

1. Open this folder in your agent tool.
2. Ask the agent to read `AGENTS.md`, `CLAUDE.md`, or `.claude/skills/career-pipeline-operator/SKILL.md`, depending on the tool.
3. Run the profile intake workflow before serious job analysis.
4. Add jobs manually, by URL, or by pasted job description.
5. Use the workflow commands in `commands.md`.

Suggested first prompt:

```text
Read AGENTS.md and workflows/01-profile-intake.md. Help me fill the user-profile files from my resume and preferences. Ask me only the questions needed to make the profile useful.
```

Example role analysis prompt:

```text
/analyze-role
Company: <company>
Role: <role>
URL: <paste URL>
Job description: <paste JD>
```

Then:

```text
/create-application-packet <company>
```

Then:

```text
/prepare-interview <company> <stage>
```

## Design principles

1. **Structured UI thinking, file-based execution.** Every AI output should become a durable object, not just a chat response.
2. **Truthful personalization.** Do not overclaim skills, experience, compensation, or prior work.
3. **User approval before external action.** Never auto-apply, auto-send emails, or commit to interviews/compensation without explicit approval.
4. **Current information must be verified.** Open roles, compensation, company status, interview processes, and legal/tax details can change.
5. **Prefer actionable next steps.** Every analysis should end with a recommendation or a clear pending question.
6. **Maintain memory explicitly.** Update files when something important changes.

## Recommended operating model

The agent should behave like a job-search operator, not a generic chatbot. It should proactively use the local workspace:

- Read candidate files before generating recommendations.
- Create or update company files after each new event.
- Save drafts in `outputs/drafts/` or the relevant company folder.
- Maintain `data/pipeline.json` and `data/next-actions.md`.
- Ask clarifying questions only when required to avoid unsafe assumptions.

## Folder map

```text
job-search-operator-skill/
  AGENTS.md                         # Codex/open agent operating instructions
  CLAUDE.md                         # Claude Code entrypoint instructions
  commands.md                       # Command-style workflow triggers
  file-conventions.md               # Naming and persistence rules
  user-profile/                     # Candidate source of truth
  workflows/                        # Step-by-step operating procedures
  templates/                        # Reusable output templates
  data/                             # Pipeline, companies, job records
  outputs/                          # Generated drafts and reports
  scripts/                          # Optional helpers for local maintenance
  .claude/skills/.../SKILL.md       # Claude-style skill wrapper
```

## What this is not

- It is not a replacement for legal, tax, or immigration advice.
- It is not an auto-apply bot.
- It is not designed to fabricate experience or optimize dishonestly.
- It is not a scraper framework by default; scraping can be added later.

## Future app mapping

These files map directly to future product entities:

| File-based object | Future app module |
|---|---|
| `user-profile/*` | Candidate profile |
| `data/jobs/*` | Role feed and fit ranking |
| `data/companies/*` | Pipeline CRM |
| `outputs/application-packets/*` | Application workspace |
| `data/companies/*/interviews.md` | Interview prep |
| `data/companies/*/offer.md` | Offer analysis |
| `data/next-actions.md` | Home dashboard |

This means you can prototype the intelligence and workflows now, then build a real UI later.
