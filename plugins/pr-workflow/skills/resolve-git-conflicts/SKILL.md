---
name: resolve-git-conflicts
description: Resolve active Git merge, rebase, cherry-pick, revert, or stash conflicts semantically. Use when Git reports unmerged paths or conflict markers and the developer wants help completing or safely aborting the operation.
---

# Resolve Git Conflicts

## Current state

1. Read repository instructions and run `git status --short --branch` plus `git diff --name-only --diff-filter=U`.
2. Inspect Git state files through `git rev-parse --git-path` to detect merge, rebase, cherry-pick, revert, or stash context; support worktrees where `.git` is a file.
3. Record the operation-specific abort command before editing.
4. Read each complete conflicted file, the base version, both sides, surrounding commits, related tests, and any rename/delete context.

## Intended action

Explain in plain language what each side intended, where the intentions conflict or compose, the proposed semantic result, and how to abort. Ask for human direction when business intent cannot be inferred safely.

## Execution

1. Edit the file into a coherent result that preserves compatible behavior from both sides. Do not choose `ours` or `theirs` blindly.
2. Remove conflict markers and inspect the resulting diff before staging each resolved path.
3. Repeat until `git diff --name-only --diff-filter=U` is empty.
4. Complete the detected operation only after validation. For multi-commit rebases or cherry-picks, repeat the lifecycle if later commits conflict.

## Validation

Search for remaining conflict markers, run focused tests for affected behavior, then repository-required checks proportional to the change. Reinspect status and the staged resolution. Do not skip an empty rebase commit automatically until its intent is understood.

## Result

Report the operation, resolved files, semantic choices, validation, final Git state, and whether the operation completed or remains paused. Keep the abort path visible while paused.

## Next action

Recommend review of the combined behavior and normal push. If a completed rebase changed published history, explain that updating the remote would require separate explicit authority for `--force-with-lease`.

## Guardrails

- Never discard one side merely to make markers disappear.
- Never run a destructive checkout/reset as a generic stash-conflict abort.
- Never force-push without explicit authority.
- Never complete an operation with failing relevant validation.
