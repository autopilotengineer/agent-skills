---
name: modernize-typescript-project
description: Audit and incrementally modernize an existing TypeScript project while preserving declared runtime and consumer compatibility. Use for tsconfig, module-format, package-layout, strictness, build, lint, test, or Node-support modernization.
---

# Modernize TypeScript Project

Read [compatibility plan](references/compatibility-plan.md) before proposing edits.

## Current state

1. Read repository instructions, manifest/lockfile, runtime pins, `tsconfig` chain, package exports, build config, source layout, tests, linting, CI, publication files, and known consumers.
2. Detect resolved TypeScript version, supported Node/browser versions, ESM/CommonJS behavior, module resolution, declaration output, strictness flags, source maps, and runtime loader assumptions.
3. Run the current clean validation path to expose baseline failures before modernization.

## Intended action

Create an incremental plan before editing. Separate compatibility constraints from accidental legacy settings, order dependent changes, identify expected breakage, define validation and rollback per step, and cite official version-specific TypeScript/Node/tool documentation.

## Execution

Only after the plan is accepted or the user explicitly requests implementation:

1. Apply the smallest coherent step, such as runtime pin alignment, isolated strictness, module-resolution correction, exports cleanup, or tool consolidation.
2. Preserve public import paths and runtime behavior unless a breaking migration is explicitly in scope.
3. Avoid combining ESM conversion, framework upgrade, test-runner replacement, and strict-mode adoption in one batch.
4. Add narrow type/runtime tests where compiler success cannot prove compatibility.

## Validation

After each step, run type checking, unit/integration tests, build, package-content inspection, declaration consumption, runtime smoke tests in supported Node versions, and source-map checks as applicable. Stop at the first failed step and keep rollback clear.

## Result

Report baseline, accepted constraints, completed steps, files changed, compatibility evidence, validation per step, deferred work, rollback, and remaining risk.

## Next action

Recommend the next independent modernization step. Keep major runtime or module-format changes in dedicated reviewed batches.

## Guardrails

- Never assume ESM is automatically better for every consumer.
- Never enable all strict flags and silence errors with broad `any` or assertions.
- Never change supported runtimes or public exports without authority.
- Never claim compiler success proves runtime or package compatibility.
