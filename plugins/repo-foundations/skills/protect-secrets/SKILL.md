---
name: protect-secrets
description: Audit and improve a repository's secret handling, ignore rules, environment examples, logging, CI, and exposure response. Use when asked to prevent credential leaks or investigate suspected secret risk without revealing values.
---

# Protect Secrets

## Current state

1. Read repository instructions, `.gitignore`, environment templates, config loaders, logging, CI workflows, deployment files, and source that reads credentials.
2. Inspect tracked filenames, staged/working diffs, and history indicators using tools that redact matches. Never print a discovered secret.
3. Classify findings as missing ignore coverage, unsafe example, hardcoded value, log/telemetry exposure, excessive CI permissions, browser/server boundary leak, or possible historical compromise.
4. Treat a real-looking credential as sensitive even if validity is unknown.

## Intended action

State the inspection scope and proposed preventive changes. If exposure is suspected, prioritize containment: stop propagation, identify the secret owner, recommend provider-side rotation/revocation, and preserve evidence without copying the value.

## Execution

When remediation is requested:

1. Improve ignore rules narrowly.
2. Create or update `.env.example` with variable names and safe placeholders only.
3. Add fail-fast environment validation and redact sensitive log fields where appropriate.
4. Recommend or configure repository-native secret scanning and least-privilege CI permissions.
5. Handle history rewriting only as a separate, explicitly authorized incident procedure after rotation; deletion from the latest commit does not revoke a leaked secret.

## Validation

Verify ignored/tracked status without echoing contents, run tests for configuration and redaction behavior, parse CI, and rescan changed paths. Report scanners used and coverage limitations.

## Result

Report categories, affected paths, severity, changes, rotation status as unknown/required/completed only with evidence, validation, and remaining history or third-party risk. Redact identifiers when they could aid misuse.

## Next action

Give exact owner-safe rotation and monitoring steps. Do not transmit, test, or revoke a credential unless explicitly authorized through an appropriate secure channel.

## Guardrails

- Never print, paste, commit, upload, or send discovered secrets.
- Never place real values in `.env.example`.
- Never claim deleting a file removes it from history or external logs.
- Never rewrite shared history or rotate production credentials implicitly.
