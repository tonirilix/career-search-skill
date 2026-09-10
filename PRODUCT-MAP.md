# Product Map: From Local Skill to App

This workspace is a prototype for the future application.

## Users

### Primary user

A job seeker who wants high-quality support across the whole job-search process, not just resume writing.

### Strong early adopter

A senior professional applying selectively to product roles, tracking multiple processes, negotiating compensation, and preparing for complex interviews.

### Secondary users

- Career changers
- Contractors/freelancers comparing offers
- Remote international candidates
- Engineers/designers/product managers with complex application processes

## Modules

1. Candidate profile
2. Role discovery
3. Fit analysis
4. Application packet
5. Pipeline CRM
6. Recruiter communication
7. Interview prep
8. Offer/contract analysis
9. Decision support
10. Weekly review

## Core flows

### Discover → Triage → Apply

1. Find or paste role
2. Normalize role
3. Score fit
4. Create application packet
5. Submit manually
6. Update pipeline

### Recruiter message → Draft → Track

1. Paste message or import email
2. Detect intent
3. Draft response
4. Save draft
5. Update company timeline
6. Set next action

### Interview scheduled → Prep → Debrief

1. Add interview stage
2. Generate prep packet
3. Practice questions
4. Record debrief
5. Update next stage

### Offer received → Analyze → Decide

1. Add offer/contract
2. Extract terms
3. Compare against profile/preferences
4. Generate clarification questions
5. Compare options
6. Recommend next action

## High-level architecture in words

The current version uses Markdown and JSON as the persistence layer. The agent reads profile files, applies workflow instructions, writes outputs, and updates pipeline files.

A future app could use the same conceptual model:

- Frontend: dashboard, role cards, pipeline board, workspaces
- Local data: SQLite or equivalent local database
- AI layer: external LLM APIs or local models
- Retrieval layer: profile, jobs, company files, notes, drafts
- Background jobs: role scans, follow-up reminders, dead-link checks
- Cloud optional: sync, job index, email/calendar integrations

## MVP

The MVP should focus on:

- Candidate profile intake
- Manual role intake
- Fit analysis
- Application packet generation
- Pipeline tracking
- Recruiter reply drafts
- Interview prep

Do not start with full auto-apply, heavy scraping, or complex integrations.

## Suggested MVP stack

### Local-agent prototype

- Markdown files
- JSON pipeline
- Claude Code / Codex / Cursor agents
- Optional Python helper scripts

### Desktop app MVP

- Electron or Tauri
- React + TypeScript
- SQLite
- Node.js or Python local service
- OpenAI/Anthropic APIs
- Optional local embeddings

### Cloud extension

- Postgres
- pgvector or Qdrant
- Background workers
- Email/calendar integrations
- Shared job index

## Monetizable features

- AI application packets
- Advanced role matching
- Interview prep packs
- Offer and contract analysis
- Recruiter email assistant
- Compensation comparison
- Follow-up automation
- Premium company/process memory
- Privacy-first local mode
- Cloud sync and multi-device access
