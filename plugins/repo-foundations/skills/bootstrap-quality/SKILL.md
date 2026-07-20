---
name: bootstrap-quality
description: Add the smallest coherent formatting, linting, type-checking, testing, and CI baseline to an existing repository. Use when a project lacks dependable local and pull-request quality checks and the developer asks to establish them.
---

# Bootstrap Quality

Read [baseline choices](references/baseline-choices.md) after detecting the stack.

## Current state

1. Read repository instructions and inspect manifests, lockfiles, runtime pins, existing scripts/configuration, representative code/tests, and CI.
2. Map what already exists for formatting, linting, types, tests, build, and pull-request enforcement.
3. Run existing checks before changing configuration so pre-existing failures are visible.

## Intended action

Propose the smallest baseline that closes demonstrated gaps. Reuse installed tools and repository conventions before adding dependencies. Explain new dependency, configuration, runtime, and developer-workflow impact.

## Execution

1. Use the repository's package manager and lockfile.
2. Configure only missing layers. Avoid replacing a functioning formatter, linter, test runner, or CI provider for preference.
3. Add clear local scripts that CI calls rather than duplicating command logic in workflow YAML.
4. Scope initial rules to catch real defects without forcing an unrelated whole-repository rewrite.
5. Add a minimal representative test when no test proves the harness works.

## Validation

Run install reproducibility when practical, each new local command separately, the aggregate CI command, and configuration syntax checks. Verify CI triggers and least-privilege permissions. Report baseline code failures separately from tooling failures.

## Result

Report reused and added tools, files changed, commands, CI behavior, exact pass/fail/skip results, migration impact, and remaining gaps.

## Next action

Recommend gradual rule tightening or coverage expansion based on observed defects, not an immediate tool migration.

## Guardrails

- Never introduce a second package manager or unnecessary framework.
- Never auto-fix unrelated code just to make the first run green.
- Never weaken checks, bypass lockfiles, or conceal failures.
- Never publish workflow changes without preserving human review gates.
