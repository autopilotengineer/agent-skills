# Security policy

## Supported versions

Security fixes are applied to the default branch. Published releases may receive fixes when a release exists and maintainers determine backporting is necessary.

## Report a vulnerability

Use this repository's GitHub Security Advisory reporting flow when available. Do not open a public issue containing credentials, exploit details, private repository data, or another person's information. If private reporting is unavailable, open a minimal public issue asking a maintainer to establish a private channel; include no sensitive details.

Include the affected skill or file, impact, safe reproduction outline, and suggested mitigation. Remove or redact credentials, tokens, private URLs, and proprietary code.

## Skill threat model

Agent Skills are instructions executed by powerful coding hosts. Reviewers should look for:

- destructive or difficult-to-reverse commands without explicit authority
- hidden external writes, forced pushes, releases, merges, or review-thread mutations
- commands that print, upload, or interpolate secrets
- overly broad filesystem, network, GitHub, database, or MCP access
- unpinned downloads, global latest-package installation, and shell injection
- instructions that bypass failing tests, hooks, approvals, or human review

Users should inspect every skill and its bundled resources before installation and retain normal host approval prompts.
