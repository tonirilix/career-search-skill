# Privacy and Publishing

## Two layers

The tracked repository is the **skill layer**: workflows, templates, scripts, documentation, and blank starter files in `workspace-template/`.

The ignored `workspace/` directory is the **private data layer**. It contains the candidate profile, resumes, role records, recruiter messages, company notes, interview preparation, offers, drafts, pipeline, and next actions.

Create the private workspace once:

```bash
python3 scripts/init_workspace.py
```

The command refuses to overwrite an existing workspace.

## Keeping the skill evergreen

Pull or merge updates to the tracked skill normally. This never changes `workspace/`. Review template changes and manually adopt useful new fields in the corresponding private record. Keep reusable improvements generic and free of real names, companies, messages, compensation, or credentials.

## Before publishing

1. Confirm `git status --ignored` shows `workspace/` as ignored.
2. Review every staged file with `git diff --cached`.
3. Use only fictional, anonymized examples.
4. Check that no live data was copied into `workspace-template/`, `examples/`, documentation, or commits.
5. If sensitive data was ever committed, remove it from the relevant remote and Git history with an appropriate repository-history remediation process before publishing.

`.gitignore` protects future untracked workspace files; it cannot remove data already present in Git history.
