---
name: recommend-mcp-servers
description: Recommend a minimal, least-privilege set of Model Context Protocol servers justified by a repository's real workflows. Use when a developer asks which MCP servers a project needs or whether MCP would improve agent work.
---

# Recommend MCP Servers

Read [server evaluation](references/server-evaluation.md) before recommending installation.

## Current state

1. Read repository instructions, stack, workflows, existing agent tools/connectors, data stores, deployment targets, and recurring verification needs.
2. Identify capability gaps rather than mapping every technology to a server.
3. Check the official MCP Registry for candidates, then inspect each server's official source, publisher, permissions, transports, maintenance, and secret handling.

## Intended action

For each actual gap, compare no server, existing local/connector tools, and a candidate MCP server. Prefer no installation when current scoped tools are sufficient.

## Execution

Produce recommendations only; install or configure a server only when separately requested. When justified, prefer:

- authoritative documentation retrieval such as Context7 for versioned package work
- GitHub MCP with read-only PR/issues/Actions tools when local GitHub access is insufficient
- Playwright MCP for real browser verification
- a database-specific server only for repositories that need database inspection, using development and read-only credentials

Avoid redundant filesystem or Git servers when the host already provides scoped local access.

## Validation

Verify each recommendation against the registry and source. Check requested scopes, default write capabilities, filesystem roots, network exposure, telemetry, credential transport, and whether tools can be narrowed or disabled.

## Result

Return a table with capability gap, recommendation, evidence, minimum toolset, credential model, access mode, risks, and safer alternative. Include an explicit `No MCP servers recommended` result when that is the correct outcome.

## Next action

Offer a least-privilege configuration plan for selected servers. Keep environment-based secrets out of committed configuration and preserve a human installation review.

## Guardrails

- Never recommend a server solely because it is popular or matches a dependency name.
- Never recommend production or write credentials when read-only development access works.
- Never invent registry status, publisher trust, or tool capabilities.
- Never expose secrets in configuration examples.
