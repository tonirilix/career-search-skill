# Scripts

Optional helper scripts for maintaining the local workspace.

These are intentionally lightweight. The skill should work even if the user never runs scripts.

## Examples

```bash
python scripts/init_workspace.py
python scripts/add_company.py <company-slug> "<role title>"
python scripts/validate_pipeline.py
```

## Notes

- Scripts should not auto-apply to jobs.
- Scripts should not send messages.
- Scripts should not upload private profile data externally.
