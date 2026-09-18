# Scripts

Optional helper scripts for maintaining the local workspace.

These are intentionally lightweight. The skill should work even if the user never runs scripts.

## Examples

```bash
python3 scripts/init_workspace.py
python3 scripts/add_company.py <company> "<role title>"
python3 scripts/validate_pipeline.py
```

## Notes

- Scripts should not auto-apply to jobs.
- Scripts should not send messages.
- Scripts should not upload private profile data externally.
- `init_workspace.py` copies the safe starter into ignored `workspace/` and never overwrites an existing workspace.
