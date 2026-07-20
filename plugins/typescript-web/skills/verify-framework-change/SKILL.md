---
name: verify-framework-change
description: Verify a proposed framework or library change against installed-version and target-version official documentation. Use before adopting an API, configuration change, upgrade, migration, or deprecation workaround when technical accuracy matters.
---

# Verify Framework Change

Read [evidence standard](references/evidence-standard.md) before researching.

## Current state

1. Read repository instructions, lockfile-resolved versions, manifests, configuration, relevant source/tests, runtime pins, and deployment assumptions.
2. Restate the proposed change and identify affected packages, APIs, configuration, build/runtime behavior, and consumers.
3. Determine both installed and target versions. If either is unknown, say so and avoid version-specific conclusions.

## Intended action

Define the exact claims to verify. Use authoritative official documentation, release notes, migration guides, API references, and source when documentation is ambiguous. Prefer version-pinned material.

## Execution

Research without editing. Identify supported behavior, breaking changes, deprecated or removed APIs, required peer/runtime versions, configuration migrations, data/build changes, and known compatibility boundaries. Search the repository for every affected usage.

## Validation

Triangulate important claims across the target docs and release/migration evidence. Label each conclusion `verified fact`, `repository evidence`, or `inference`. When practical, design or run a read-only reproduction against the installed project; never substitute a latest-version example for installed behavior.

## Result

Return a decision: `supported`, `supported with migration`, `not supported`, or `insufficient evidence`. Include version matrix, affected files/usages, breaking changes, exact migration and validation steps, source links, unknowns, and rollback considerations. Do not modify code.

## Next action

Offer an incremental implementation plan or a focused proof of concept. Keep actual dependency/code changes separately reviewable.

## Guardrails

- Never rely on memory for current version behavior when official sources are available.
- Never cite unofficial tutorials as authority for framework contracts.
- Never hide inference behind confident language.
- Never install global latest packages or mutate the lockfile during verification.
