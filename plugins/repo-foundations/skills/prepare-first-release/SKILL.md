---
name: prepare-first-release
description: Assess and prepare a repository for its first reproducible public or internal release. Use when a developer asks for release readiness, packaging checks, or a first-release plan; create a tag or release only with explicit authorization.
---

# Prepare First Release

## Current state

1. Read repository instructions, README, license, security policy, contribution guide, manifests, packaging config, version files, CI, changelog/release automation, and ignore rules.
2. Detect the release artifact, supported platforms/runtimes, installation path, version source, repository visibility, and publication registry or GitHub-only model.
3. Inspect Git status, remote default branch, tags, branch protections when visible, and reproducible build inputs.

## Intended action

State the intended audience and artifact, required readiness gates, validation plan, and whether work is report-only or includes authorized fixes. Release creation is out of scope unless the user explicitly authorizes it.

## Execution

Verify or improve, when requested:

- clear value proposition and installation/usage instructions
- correct Apache or project-selected license and notices
- security reporting and contribution process
- semantic version source and changelog/release notes
- packaging contents and exclusion rules
- deterministic install, validation, build, and artifact creation
- CI on the real default branch and documented publishing permissions

Do not add release automation more complex than the project needs.

## Validation

Run the clean-checkout-equivalent install and validation, build/package dry run, artifact-content inspection, and install smoke test when available. Verify docs commands and links. Record pass, fail, warning, and skip with exact evidence.

## Result

Produce a release-readiness report with blocking issues first, completed fixes, artifact/version details, reproducibility evidence, security and rollback considerations, and an explicit `READY` or `NOT READY` conclusion.

## Next action

If ready, show the exact proposed tag and release command and wait for release authorization. If not ready, recommend the smallest blocking fix. Never create `v0.1.0` or any release implicitly.

## Guardrails

- Never tag, publish, create a GitHub release, or change visibility without explicit authority.
- Never publish from a dirty or unvalidated tree.
- Never omit license/security gaps from a public-readiness report.
- Never claim reproducibility without a clean build or a clearly labeled skip.
