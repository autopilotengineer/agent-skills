# GitHub review threads

Use `gh pr view` to identify repository, PR number, head, and base. Prefer GitHub's GraphQL `reviewThreads` connection because REST review comments alone do not expose reliable thread resolution state.

For each thread retain:

- thread node ID, `isResolved`, and `isOutdated`
- comment node/database ID, body, author, path, line, original line, and timestamps
- replies and the latest commit or diff context

Paginate beyond the first page. Treat missing authentication, no PR for the branch, insufficient permissions, and rate limits as distinct blockers. Mutations such as replies and `resolveReviewThread` are external writes: perform them only after the skill's execution and validation gates. Re-query afterward to confirm server state rather than assuming the mutation succeeded.
