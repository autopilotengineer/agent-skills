---
name: repo-doctor
description: Diagnose a software repository's stack, workflows, delivery setup, and missing safeguards without modifying it. Use for repository health checks, onboarding assessments, or prioritized recommendations before engineering work begins.
---

# Repository Doctor

Read [stack signals](references/stack-signals.md) when the repository is unfamiliar or polyglot.

## Current state

1. Read all applicable `AGENTS.md`, `CLAUDE.md`, README, contribution, and security guidance.
2. Inventory top-level and package-level manifests, lockfiles, runtime pins, source, scripts, test configuration, CI, database files, container/deployment configuration, and environment handling.
3. Detect the stack, framework, package manager, monorepo boundaries, runtime versions, build/lint/typecheck/test commands, database, deployment target, and release mechanism from evidence.
4. Mark conflicting or missing evidence as unknown; do not guess.

## Intended action

State the detected repository shape, inspection scope, and diagnostic commands. Keep all actions read-only unless the user separately asks for remediation.

## Execution

Evaluate whether a new developer and CI can reproducibly install, validate, build, run, configure, and release the project. Check for inconsistent runtimes, multiple lockfiles, undocumented environment variables, missing tests or CI gates, unsafe defaults, stale instructions, generated-file drift, and package-boundary gaps.

## Validation

Cross-check claimed commands against manifests and CI. Run safe version/help/status commands and non-mutating checks when useful. Distinguish confirmed failures from risks inferred from missing evidence.

## Result

Report:

1. Detected stack and repository map with evidence paths.
2. What already works.
3. Findings ordered `critical`, `high`, `medium`, `low`.
4. Exact next action for each finding, including file or command.
5. Unknowns, skipped checks, and remaining risk.

Do not create a wall of generic best practices; connect every recommendation to repository evidence.

## Next action

Recommend the smallest high-value remediation and ask whether to implement it. Do not modify the repository during the diagnosis.

## Guardrails

- Inspect before editing and preserve unrelated work.
- Never install tools, change dependencies, or run destructive database/deployment commands during an audit.
- Never expose environment values or credentials.
- Never claim a command works unless evidence or execution proves it.
