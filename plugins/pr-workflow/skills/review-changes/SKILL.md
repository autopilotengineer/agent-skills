---
name: review-changes
description: Perform an evidence-backed code review of local or pull-request changes against the correct merge base. Use when asked to review, critique, or find risks in a diff; this skill reports findings and does not implement fixes.
---

# Review Changes

## Current state

1. Read repository instructions and determine whether the target is a PR, branch, commit range, staged diff, or working tree.
2. Discover the base from PR metadata when available; otherwise use the upstream/default branch and verify it with the remote. Fetch read-only refs when permitted.
3. Compute `git merge-base <base> <head>` and review the complete diff from that commit. Include staged, unstaged, and relevant untracked work only when the requested target includes it.
4. Read full changed files, callers, schemas, migrations, tests, and configuration needed to understand behavior.

## Intended action

State the review target, merge base, changed scope, validation available, and risk areas. Prioritize correctness, regressions, security, data loss, concurrency, observability, compatibility, and missing tests over style preferences.

## Execution

Trace each behavioral change through inputs, state transitions, error paths, and consumers. Verify suspected problems with repository evidence or a focused read-only command. Distinguish defects from questions and optional improvements.

Do not edit code, commit, push, or resolve comments unless the user separately requests a fix.

## Validation

For each finding, verify the affected path and tight line range, the triggering conditions, the observable impact, and why existing tests or guards do not prevent it. Drop speculative findings that cannot be supported.

## Result

List findings first, ordered by severity:

- `P0` immediate catastrophic impact
- `P1` serious correctness, security, or data-loss risk
- `P2` meaningful defect or regression
- `P3` bounded maintainability or test gap

Each finding must include a concise title, file and line, evidence, impact, and suggested direction. Then list open questions and a short validation summary. If no findings remain, say so and name residual risks or untested areas.

## Next action

Offer to implement selected findings, add tests, or re-review a revised diff. Keep the review decision with the human.

## Guardrails

- Never review against an assumed `main` branch.
- Never report style-only preferences as correctness defects.
- Never claim validation ran when it did not.
- Never expose secrets encountered in diffs or configuration.
