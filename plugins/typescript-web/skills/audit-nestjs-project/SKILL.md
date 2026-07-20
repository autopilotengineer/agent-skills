---
name: audit-nestjs-project
description: Audit an existing NestJS service's modules, dependency injection, configuration, request safety, auth, persistence, tests, and deployment readiness using official version-matched documentation. Use for NestJS architecture or production-readiness reviews.
---

# Audit NestJS Project

Read [NestJS audit evidence](references/audit-evidence.md) after detecting the project choices.

## Current state

1. Read repository instructions, manifest/lockfile, Nest CLI config, TypeScript config, bootstrap, root modules, representative feature modules/controllers/providers, persistence, auth, tests, CI, and deployment files.
2. Detect resolved NestJS version, Node version, Express or Fastify adapter, package manager, monorepo mode, persistence library, authentication strategy, validation approach, logger, and test runner.
3. Retrieve official NestJS and first-party adapter documentation matching the installed or target version. Mark third-party behavior separately.

## Intended action

State detected architecture, request path, trust boundaries, documentation sources, audit scope, and unknowns before proposing changes.

## Execution

Review module boundaries, provider scopes and injection tokens, circular dependencies, configuration validation, DTO transformation/validation, exception filters, authentication, authorization, guards/interceptors/pipes order, logging and correlation, persistence/transaction boundaries, graceful shutdown, health checks, tests, build output, and deployment assumptions.

## Validation

Run documented read-only or validation commands when practical. Trace at least one success and failure path from transport to persistence. Support each finding with code evidence and version-appropriate official guidance; distinguish framework requirements from preferred architecture.

## Result

Report findings by severity with path/line, affected request or operational scenario, impact, official evidence, and smallest remediation. Include strengths, missing validation/configuration, test gaps, deployment unknowns, and exact command results. Do not edit during an audit.

## Next action

Propose an incremental remediation plan, starting with request validation, auth, data integrity, or operability risks. Implement only when requested.

## Guardrails

- Never infer global pipes, guards, filters, or interceptors without reading bootstrap/module registration.
- Never treat TypeScript types as runtime validation.
- Never recommend request-scoped providers casually; assess cost and necessity.
- Never expose secrets from configuration or logs.
