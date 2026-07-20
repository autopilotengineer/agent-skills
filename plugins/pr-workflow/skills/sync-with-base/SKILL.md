---
name: sync-with-base
description: Safely update the current Git branch from its real base branch using an informed merge or rebase. Use when a developer asks to sync, update, catch up, or incorporate upstream base changes.
---

# Sync With Base

## Current state

1. Read repository instructions and inspect branch, status, remotes, upstream tracking, and active Git operations.
2. Detect detached HEAD and stop with recovery guidance.
3. Discover the base from an existing PR, explicit branch configuration, upstream relationship, or remote default branch. Verify remote refs; never assume `main`.
4. Protect staged, unstaged, and untracked work. Do not auto-stash without explaining ownership and obtaining authority.
5. Fetch the relevant remote and report ahead/behind counts and changed upstream paths.

## Intended action

Explain the chosen base and strategy:

- Merge preserves published commit identities and adds a merge commit.
- Rebase creates a linear history but rewrites feature commits and may require a later force-with-lease push.

Follow repository policy or the user's choice. Prefer merge for a shared published branch when no policy is clear; stop for a material history decision.

## Execution

1. Preserve dirty work using an explicitly approved checkpoint or named stash.
2. Run `git merge <remote>/<base>` or `git rebase <remote>/<base>` as chosen.
3. On conflicts, show the abort command and invoke semantic conflict resolution. Stop if intent is ambiguous.
4. Restore only the stash created for this operation and report any restore conflicts separately.

## Validation

Run `git status --short --branch`, verify the base is an ancestor of `HEAD`, inspect the resulting history, and run relevant validation for conflict resolutions or changed generated artifacts.

## Result

Report base, strategy, before/after ahead-behind state, conflict handling, restored work, validation, and whether local history now differs from the remote branch.

## Next action

Recommend normal push after a merge. After a rebase of published commits, explain the risk and wait for explicit authority before any `git push --force-with-lease`.

## Guardrails

- Never select a base solely from a hardcoded candidate list.
- Never lose or mix dirty work.
- Never auto-resolve semantic conflicts or force-push.
- Never claim synchronization when fetch or validation failed.
