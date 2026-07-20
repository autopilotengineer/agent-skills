---
name: bootstrap-typescript-service
description: Establish a production-shaped TypeScript service baseline in a greenfield or existing repository. Use when asked to create or harden a backend service with strict types, runtime validation, configuration, health checks, structured errors/logging, tests, and CI.
---

# Bootstrap TypeScript Service

Read [service baseline](references/service-baseline.md) after detecting whether the repository is greenfield or existing.

## Current state

1. Read repository instructions and inspect all existing files, manifests, lockfiles, runtime pins, framework choices, deployment target, CI, and neighboring services.
2. Classify the target as greenfield, an existing service needing hardening, or a package inside a monorepo.
3. Detect established package manager, TypeScript/runtime versions, module format, HTTP framework, validation/logging/test tools, and operational conventions.
4. Run existing validation before editing when a service already exists.

## Intended action

Propose the smallest production-shaped baseline compatible with the repository. Explain the request flow, configuration contract, failure model, health semantics, test layers, CI commands, and any new dependencies. Avoid inventing queues, databases, ORMs, containers, or layers without a requirement.

## Execution

1. Reuse repository choices. For greenfield work, select stable minimal dependencies with official documentation and explicit runtime support.
2. Enable strict typing without unsafe escape hatches.
3. Validate external input and environment configuration at runtime.
4. Add structured errors and logs with redaction, graceful shutdown, liveness/readiness endpoints, and a small composable application boundary.
5. Add unit plus request-level tests, deterministic local scripts, and pull-request CI.
6. Keep business logic independent from transport only where real behavior exists; do not scaffold speculative architecture.

## Validation

Run clean install, formatting/lint, type checking, tests, build, start/health smoke test, invalid-config failure, invalid-request behavior, graceful shutdown, and package/artifact inspection as applicable. Record exact pass/fail/skip results.

## Result

Report architecture, files/dependencies, commands, configuration variables by name only, endpoint behavior, validation evidence, operational assumptions, and deferred capabilities.

## Next action

Recommend adding the first real use case and its acceptance test before expanding infrastructure.

## Guardrails

- Never commit real secrets or log sensitive values.
- Never add unnecessary architecture or switch established tools without evidence.
- Never confuse TypeScript types with runtime input validation.
- Never claim production readiness when deployment, persistence, or failure behavior remains untested.
