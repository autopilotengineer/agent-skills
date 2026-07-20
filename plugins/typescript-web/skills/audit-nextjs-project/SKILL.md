---
name: audit-nextjs-project
description: Audit an existing Next.js application's architecture, security, accessibility, testing, and deployment readiness using documentation matched to its installed version and router. Use for Next.js project reviews before proposing code changes.
---

# Audit Next.js Project

Read [Next.js audit evidence](references/audit-evidence.md) after detecting the installed version and router.

## Current state

1. Read repository instructions, package/workspace manifests, lockfile, Next.js config, TypeScript config, environment examples, CI, deployment files, and representative routes/components/tests.
2. Detect the resolved Next.js and React versions, package manager, Node support, App Router (`app/`), Pages Router (`pages/`), or hybrid use. Detect output mode, hosting assumptions, middleware/proxy, authentication, and data layer.
3. Use current official Next.js and React documentation that matches the installed or explicitly targeted version. Record exact documentation URLs and version applicability.

## Intended action

State audit scope, router/version, deployment model, evidence sources, and unknowns. Audit before suggesting edits.

## Execution

Trace representative user journeys and review routing/layout composition, Server and Client Component boundaries, data access, mutations, caching and revalidation, runtime selection, metadata, error/not-found/loading behavior, authentication and authorization, secret boundaries, accessibility, tests, observability, and deployment assumptions.

## Validation

Run documented non-mutating checks when practical. Verify each finding against code plus version-matched official guidance. Distinguish confirmed defects, documentation mismatches, project-specific tradeoffs, and inference. Account for App and Pages Router differences rather than applying one router's rules to the other.

## Result

List evidence-backed findings by severity with file/line, affected route or user flow, impact, official reference, and smallest remediation direction. Then report strengths, unknowns, validation results, and residual risks. Do not modify code during an audit.

## Next action

Propose a prioritized remediation sequence with focused tests. Implement only if separately requested.

## Guardrails

- Never assume all components should be Server Components or Client Components.
- Never describe caching behavior from memory when version-specific docs can verify it.
- Never recommend moving secrets into client-exposed variables.
- Never claim deployment readiness without checking the actual target and runtime.
