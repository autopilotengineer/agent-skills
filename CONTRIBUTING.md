# Contributing

Contributions should make AI-assisted engineering safer, clearer, and more portable without turning skills into generic textbooks.

## Before editing

1. Open an issue or describe the concrete developer request and failure mode the change addresses.
2. Read `AGENTS.md`, the target `SKILL.md`, its references, and relevant evaluation scenarios.
3. Preserve unrelated work and avoid host-specific assumptions in the skill body.

## Add a skill

Use the installed `skill-creator` workflow. Initialize the folder with its `scripts/init_skill.py` command so the required `SKILL.md` and `agents/openai.yaml` start from valid templates. Place the skill under the narrowest pack:

```text
plugins/<pack>/skills/<skill-name>/
```

Do not hand-build a new skill folder. Do not add README, installation, or changelog files inside it.

## Authoring contract

- Use only `name` and `description` in `SKILL.md` frontmatter.
- Match the folder and skill name; use lowercase kebab-case.
- Keep the description narrow enough not to compete with neighboring skills.
- Include the visible lifecycle `Current state → Intended action → Execution → Validation → Result → Next action`.
- Inspect before editing, preserve unrelated work, and use the real default branch and repository conventions.
- Use official version-appropriate sources for external technology claims.
- Put detailed variants in directly linked, one-level `references/` files.
- Keep `SKILL.md` below 500 lines and free of authoring scaffolds.
- Never expose secrets or silently weaken validation and review gates.

## Test

Run:

```bash
python3 scripts/validate_repository.py
```

Run the `skill-creator` `quick_validate.py` against every changed skill. If installed, also run:

```bash
claude plugin validate .
gh skill publish --dry-run
```

Add scenario fixtures under `evals/scenarios/` for success, failure, ambiguous intent, permissions, stale state, and validation failure as applicable.

## Pull requests

Use a Conventional Commit. The pull request should explain what changed, why, impact, root cause when relevant, implementation details, exact test steps, and explicit pass/skip/warning results. Open as a draft until validation and human review are complete.
