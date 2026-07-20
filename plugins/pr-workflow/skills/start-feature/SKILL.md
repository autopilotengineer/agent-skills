---
name: start-feature
description: Safely start focused Git work on a new branch. Use when a developer asks to begin a feature, fix, spike, or task and needs the repository updated without losing dirty work or assuming the default branch is main.
---

# Start Feature

## Current state

1. Confirm the working directory is inside a Git repository.
2. Read `AGENTS.md`, `CLAUDE.md`, contribution guidance, and branch conventions before changing state.
3. Run `git status --short --branch`, `git branch --show-current`, and `git remote -v`.
4. Detect detached HEAD. Stop and explain recovery choices before creating a branch.
5. Discover the remote default branch from `refs/remotes/<remote>/HEAD`; if missing, query the remote with `git ls-remote --symref <remote> HEAD`. Never infer that it is `main`.
6. If tracked, staged, or untracked work exists, identify its purpose. Do not stash, commit, move, or discard it without the user's authority.

## Intended action

State the detected default branch, current branch, dirty-work status, remote, and proposed branch name. Normalize a short task description into the repository's established convention; otherwise prefer `feature/<short-slug>` for features and `fix/<short-slug>` for fixes.

## Execution

1. Fetch the chosen remote without pruning or deleting refs unless requested.
2. Switch to the local default branch, creating it to track the remote only when needed.
3. Update it with `git pull --ff-only <remote> <default-branch>`. Stop if fast-forward is impossible.
4. Create the focused branch with `git switch -c <branch-name>`.
5. If dirty work was explicitly preserved through a user-approved stash, restore only that stash and report conflicts.

## Validation

Run `git status --short --branch`, `git branch --show-current`, and `git merge-base --is-ancestor <remote>/<default-branch> HEAD`. Verify the original work is still present when applicable.

## Result

Report the branch name, starting commit, default branch, remote, dirty-work handling, and validation evidence. Never say the branch is current if fetch or fast-forward failed.

## Next action

Tell the developer they can begin the scoped change. If blocked, give the exact safe recovery command and explain it in beginner-friendly language.

## Guardrails

- Inspect before editing and preserve unrelated work.
- Never delete a branch, discard changes, or force-update history.
- Keep progress and diagnostics on stderr in any helper script; reserve stdout for results.
- Never expose credentials embedded in remote URLs.
