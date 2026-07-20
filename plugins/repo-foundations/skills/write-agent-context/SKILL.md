---
name: write-agent-context
description: Create or improve concise repository guidance for coding agents in AGENTS.md or CLAUDE.md. Use when a developer asks to document project commands, architecture, conventions, or safety rules for AI-assisted development.
---

# Write Agent Context

## Current state

1. Read every applicable existing agent instruction file from repository root to the relevant package.
2. Inspect README, contribution guidance, manifests, lockfiles, CI, representative source and tests, configuration, and existing architecture documents.
3. Identify the host-neutral facts agents need repeatedly: purpose, structure, exact commands, conventions, boundaries, generated files, validation, and dangerous operations.
4. Preserve existing instructions and note conflicts or stale claims before editing.

## Intended action

Propose one source of truth and thin compatibility pointers. Prefer the established canonical file; if none exists and multiple hosts are expected, prefer a concise root `AGENTS.md` with a thin `CLAUDE.md` pointer when needed. Explain which documents are warranted by repository complexity.

## Execution

1. Write concise, evidence-based instructions using exact runnable commands.
2. Keep critical rules close to the code they govern through scoped instruction files only when package behavior genuinely differs.
3. Link to existing detailed docs instead of duplicating them.
4. Generate architecture, testing, dependency, or standards documents only when the repository needs durable detail that would make the primary context file unwieldy.
5. Do not erase user-authored guidance; merge carefully and call out unresolved contradictions.

## Validation

Verify every path and command, ensure pointers resolve, check that nested guidance does not contradict root guidance, and review the diff for generic filler or duplicated prose.

## Result

Report files created or changed, evidence used, preserved instructions, verified commands, unresolved unknowns, and any additional documents deliberately not created.

## Next action

Recommend a human review of project intent and the first real task that should test whether the guidance is sufficient.

## Guardrails

- Never invent architecture, conventions, or commands.
- Never maintain two full copies of the same instructions.
- Never expand a small repository into a documentation suite without evidence.
- Never include secrets, personal paths, or host-specific assumptions unless the repository requires and documents them.
