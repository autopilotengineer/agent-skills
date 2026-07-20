# NestJS audit evidence

Inspect official documentation for the detected major version and platform adapter.

| Area | Evidence to trace |
| --- | --- |
| Composition | Root/feature modules, dynamic modules, exports, injection tokens, provider scopes, cycles |
| Request safety | Bootstrap options, global and route pipes, DTO decorators, transformation, whitelisting |
| Failures | Domain errors, HTTP mapping, filters, logging, response contracts |
| Access | Authentication strategy, guard order, authorization metadata/policies, public-route exceptions |
| Persistence | Repository/service boundary, transaction ownership, migrations, retries, idempotency |
| Operations | Structured logger, request IDs, health/readiness, graceful shutdown, runtime/container config |
| Tests | Unit module setup, provider overrides, integration/e2e app bootstrap parity, database isolation |

For Fastify, verify plugin and middleware compatibility rather than assuming Express behavior. For monorepos, identify app/library boundaries and the command that validates each affected project.
