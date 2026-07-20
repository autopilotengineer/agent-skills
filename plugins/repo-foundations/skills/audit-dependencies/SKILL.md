---
name: audit-dependencies
description: Audit declared, installed, and available dependency versions and plan or perform safe incremental upgrades. Use for outdated packages, security updates, peer conflicts, or major-version migrations; do not use for casual package installation.
---

# Audit Dependencies

Read [upgrade evidence](references/upgrade-evidence.md) before recommending or applying version changes.

## Current state

1. Read repository instructions, manifests, lockfiles, runtime pins, workspace configuration, CI, and dependency policy.
2. Identify the actual package manager from the lockfile and manifest metadata.
3. Record declared ranges, lockfile-resolved versions, workspace consumers, peer requirements, overrides, and currently available versions.
4. Run the ecosystem's read-only outdated/audit commands without printing tokens or private-registry credentials.

## Intended action

Separate:

- compatible patch/minor updates
- security-driven updates
- peer or runtime constraint conflicts
- breaking major updates that need migration work

Treat “latest” as a target to investigate. Cite official version-specific documentation, release notes, and migration guides. Distinguish verified facts from inference.

## Execution

If the user requested changes, upgrade small coherent batches with the existing package manager. Start with safe independent updates, then handle coupled framework/tooling migrations separately. Inspect lockfile changes and do not add global packages or use unpinned `latest` installers.

## Validation

After every batch, run install integrity, focused tests, types/lint, build, and relevant integration checks. Stop on peer conflicts or regressions, identify the responsible batch, and keep rollback straightforward. Do not stack later upgrades on a failing batch.

## Result

Report current/target versions, evidence links, compatibility classification, applied batches, validation per batch, deferred majors, rollback commands, and remaining security/operational risk.

## Next action

Recommend the next lowest-risk batch or a dedicated migration plan. Keep breaking upgrades reviewable and reversible.

## Guardrails

- Never switch package managers, delete a lockfile, or install all latest versions blindly.
- Never use vulnerability output as proof that an automatic breaking fix is safe.
- Never expose registry credentials or environment values.
- Never claim compatibility without version-matched evidence and validation.
