---
name: checkpoint-work
description: Review, validate, stage, and commit a coherent local change. Use when a developer asks to save, checkpoint, or commit work; do not use merely to review changes or open a pull request.
---

# Checkpoint Work

Read [validation discovery](references/validation-discovery.md) when repository validation is not already documented.

## Current state

1. Read repository instructions and confirm the Git root, branch, and remote default branch.
2. Inspect `git status --short`, `git diff --stat`, `git diff`, `git diff --cached`, and relevant untracked files. Review the complete diff, not only a summary.
3. Group files by purpose. Flag unrelated edits, generated output, vendored files, large binaries, lockfile changes, and conflict markers.
4. Scan names and diff content for likely secrets without echoing discovered values. If exposure is suspected, stop staging and recommend rotation and history review.

## Intended action

Describe the single coherent change to commit, the exact files intended for staging, validation to run, and files intentionally excluded. If the work contains independent concerns, propose separate checkpoints.

## Execution

1. Run focused validation first, then the checkout-appropriate broader checks discovered from repository evidence.
2. Stage explicit paths or use patch staging. Never default to `git add -A` in a mixed worktree.
3. Reinspect `git diff --cached --stat` and `git diff --cached`.
4. Create a Conventional Commit whose type and scope match the staged change, for example `fix(auth): reject expired sessions`.
5. Let hooks run normally. Do not bypass them to manufacture a successful commit.

## Validation

Verify the commit with `git show --stat --oneline --decorate HEAD`, rerun `git status --short`, and confirm excluded files remain untouched. Report every command as pass, fail, warning, or skip with a reason.

## Result

Report the commit SHA and subject, included files, remaining worktree changes, and exact validation results. Never claim a clean worktree unless `git status` proves it.

## Next action

Suggest the next smallest step: continue working, create another checkpoint for a separate concern, review the branch, or submit a pull request.

## Guardrails

- Never stage secrets, unrelated work, or generated files without evidence they belong.
- Never amend, squash, or rewrite an existing commit unless explicitly requested.
- Never conceal failing hooks or tests.
- Preserve human review gates and explain failures accurately in plain language.
