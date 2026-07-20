---
name: submit-pull-request
description: Prepare, validate, push, and open a detailed draft GitHub pull request for the current branch. Use when a developer explicitly asks to submit, create, or open a PR; do not use for review-only requests or direct merging.
---

# Submit Pull Request

## Current state

1. Read repository and contribution instructions. Verify `git`, the remote, and authenticated GitHub CLI access.
2. Detect detached HEAD, the current branch, remote default branch, and any existing PR for the branch.
3. Determine the PR base from explicit intent, existing PR metadata, branch configuration, or the remote default branch—in that order.
4. Inspect status, commits, and the complete diff from the verified merge base. Include untracked files in the scope review.
5. Identify unrelated changes, generated artifacts, accidental secrets, missing commits, and whether the branch is behind its base.

## Intended action

State the head/base pair, change sets, validation plan, push target, and whether separate PRs are needed. Split unrelated concerns before submission when it can be done without rewriting shared history; otherwise stop for a material scope decision.

## Execution

1. Checkpoint intended local work coherently; never sweep a mixed worktree into one commit.
2. Run focused and checkout-appropriate validation. Record pass, fail, warning, and skip results exactly.
3. Push with upstream tracking. Do not force-push or change the base silently.
4. Create a draft PR by default. If a PR already exists, update or report it rather than creating a duplicate.
5. Build the PR body with: what changed, why, user/developer impact, root cause when relevant, implementation details, exact test steps, and explicit pass/skip/warning notes. Include screenshots or migration/rollback notes only when applicable.

## Validation

Verify the remote branch SHA, PR URL, title, draft state, head, base, and rendered body. Confirm local uncommitted work was not accidentally included.

## Result

Report repository, branch, commit SHA, PR URL, draft state, validation matrix, and any remaining reviewer actions. Never describe a skipped check as passing.

## Next action

Recommend human review and the most useful reviewer verification step. Do not mark ready, merge, release, or publish unless separately authorized.

## Guardrails

- Treat push and PR creation as authorized only by an explicit submission request.
- Never push secrets, rewrite history, or bypass branch protection.
- Preserve unrelated work and human review gates.
- Explain authentication or validation failures with exact recovery commands.
