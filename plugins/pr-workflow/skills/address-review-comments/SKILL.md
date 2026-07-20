---
name: address-review-comments
description: Triage and address unresolved GitHub pull-request review feedback in coherent, verified batches. Use when asked to fix, answer, or resolve PR review comments, optionally with a bounded monitoring period for new feedback.
---

# Address Review Comments

Read [GitHub review threads](references/github-review-threads.md) before querying or mutating thread state.

## Current state

1. Read repository instructions, confirm authenticated GitHub access, and find the PR for the current branch or supplied PR identifier.
2. Fetch unresolved review threads plus top-level review and issue comments. Preserve thread IDs, comment IDs, authors, timestamps, paths, lines, resolution state, and outdated state.
3. Read the full current file, nearby tests, relevant callers, and later commits for every actionable comment.
4. Classify every item as `code change`, `question`, `disagreement`, `already fixed`, `outdated`, or `human input required`. Never silently omit feedback.

## Intended action

Present the classification, proposed file-based batches, planned replies, validation, and blockers. Conflicting requests or architectural decisions require explicit human direction unless repository evidence clearly resolves them.

## Execution

1. Apply the smallest coherent batches, preserving style and unrelated work.
2. Add or update tests that demonstrate behavioral fixes.
3. Validate each batch, inspect its complete diff, commit intentionally, and push normally.
4. Only after the fix is pushed and verification passes, reply with concrete evidence and resolve the corresponding thread when resolution is authorized.
5. For questions or disagreements, reply only with evidence-backed reasoning. Leave the thread unresolved when a reviewer or human decision remains necessary.

## Validation

Run focused checks and the broader repository-required suite. Re-fetch thread state and compare pushed SHA to the verified commit. Treat failing tests after a proposed fix as a failed batch: do not push, reply `fixed`, or resolve its thread.

## Result

Report every thread and its classification, action, commit, reply/resolution status, and validation. List unresolved, outdated, conflicting, and human-blocked feedback explicitly.

## Next action

If the user requested monitoring, use a bounded duration or number of polls they approved; stop early when no new actionable comments appear. Do not impose a fixed five-minute wait. Otherwise hand control back for reviewer follow-up.

## Guardrails

- Never resolve a thread before the pushed fix is verified.
- Never treat outdated as automatically fixed.
- Never force-push, merge, or conceal validation failure.
- Never transmit secrets in replies, logs, or queries.
