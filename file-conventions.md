# File Conventions

## Slugs

Use lowercase kebab-case:

- `sezzle`
- `eden`
- `clara-senior-frontend`
- `dropbox-ic4-loop`

## Dates

Use ISO dates in filenames:

- `2026-09-09-eden-recruiter-reply.md`
- `2026-09-09-weekly-review.md`

## Company folder

Every active company should have:

```text
data/companies/<company>/
  process.md
  role.md
  recruiter-messages.md
  interviews.md
  offer.md
  notes.md
```

Optional:

```text
  contract-notes.md
  application.md
  decision-memo.md
  references.md
```

## Role analysis file

Use:

```text
data/jobs/analyzed/<company>-<role-slug>.md
```

## Application packets

Use:

```text
outputs/application-packets/<company>/
  cover-letter.md
  form-answers.md
  positioning-notes.md
  submission-checklist.md
```

## Draft replies

Use:

```text
outputs/drafts/<date>-<company>-<purpose>.md
```

Examples:

```text
outputs/drafts/2026-09-09-sezzle-pto-clarification.md
outputs/drafts/2026-09-09-eden-ceo-thank-you.md
```

## Status values

Use one of:

- `found`
- `saved`
- `applied`
- `recruiter-screen`
- `technical-screen`
- `onsite-loop`
- `final-round`
- `offer`
- `accepted`
- `rejected`
- `withdrawn`
- `inactive`

## Source labels

Every important fact should be labeled where possible:

- `source: user-provided`
- `source: job description`
- `source: recruiter message`
- `source: web verified`
- `source: inferred`
- `source: unverified`

## Do not bury important facts in chat

If something changes, update the appropriate file.

Examples:

- salary quoted to recruiter
- interview scheduled
- application submitted
- offer deadline
- concern or red flag
- accepted/rejected/withdrawn status
