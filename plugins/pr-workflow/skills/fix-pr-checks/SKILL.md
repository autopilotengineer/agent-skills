---
name: fix-pr-checks
description: Diagnose and fix failing GitHub Actions checks on a pull request. Use when a developer asks to investigate red CI checks, reproduce the first actionable failure, and implement a minimal verified correction.
---

# Fix PR Checks

## Current state

1. Read repository instructions and verify GitHub CLI authentication, the target PR, head SHA, base branch, and local worktree state.
2. Inspect all check conclusions, then fetch failed job and step logs. Separate actionable failures from cancellations, infrastructure outages, flaky retries, and downstream failures.
3. Identify the first causal failure in execution order. Read the workflow at the checked-out commit and the code/config it invokes.

## Intended action

State the failing check, first actionable error, evidence for the root cause, proposed smallest fix, reproduction command, and validation plan. Mark uncertainty explicitly.

## Execution

1. Reproduce locally when practical using the repository's actual runtime, package manager, lockfile, environment contract, and command.
2. Implement only the causal fix. Do not change CI configuration merely to hide an application, test, dependency, or environment failure.
3. Add or adjust a test when it provides durable regression coverage.
4. Inspect the complete diff, checkpoint coherently, and push only when the request includes fixing the PR and validation passes.

## Validation

Rerun the focused reproduction, then broader checkout-appropriate checks. After push, verify the remote SHA and observe the new check run when practical. Never claim CI passes based only on a local result.

## Result

Report the root cause, changed files, commit/push state, local validation, remote check state, and any infrastructure or flaky failures left untouched.

## Next action

If remote checks are still running, offer bounded monitoring. If they fail differently, restart diagnosis from the new first actionable cause rather than layering speculative changes.

## Guardrails

- Never expose secrets from Actions logs.
- Never disable, skip, or weaken a check to turn it green without explicit justified authority.
- Never edit unrelated workflows or regenerate lockfiles casually.
- Never force-push or conceal a local/remote mismatch.
