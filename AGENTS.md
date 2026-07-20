# Repository guidance

This repository publishes portable Agent Skills in three Claude-compatible plugin packs.

## Required workflow

- Read the open Agent Skills specification before changing format assumptions.
- Initialize new skill folders with the installed `skill-creator` initializer; do not hand-build them.
- Keep `SKILL.md` frontmatter to `name` and `description` only.
- Preserve the lifecycle `Current state → Intended action → Execution → Validation → Result → Next action`.
- Keep host-specific distribution metadata outside skill instructions.
- Put detailed variants in one-level `references/` files and keep every `SKILL.md` under 500 lines.
- Do not add README, changelog, or installation files inside skill folders.

## Validate

```bash
python3 scripts/validate_repository.py
gh skill publish --dry-run
```

Also run the `skill-creator` `quick_validate.py` against every changed skill before publishing.
