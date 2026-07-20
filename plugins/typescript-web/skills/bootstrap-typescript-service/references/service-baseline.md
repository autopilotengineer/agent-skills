# Service baseline

A minimal production-shaped service should make these boundaries explicit:

- **Process:** supported Node version, deterministic build/start, signal handling, nonzero startup failure.
- **Configuration:** schema-validated environment names, defaults only when safe, no values logged.
- **Transport:** request IDs, bounded payloads/timeouts where supported, runtime input validation, stable error envelope.
- **Application:** small dependency surface and testable use-case logic; add abstraction only around real boundaries.
- **Operations:** structured redacted logs, liveness, readiness based on actual dependencies, graceful shutdown.
- **Quality:** formatting check, lint, strict type check, unit tests, request-level smoke test, build, pull-request CI.

Add a database, migration tool, authentication, metrics, tracing, container, or deployment manifest only when required by the intended service or surrounding repository. Document which omitted capabilities become necessary before real production traffic.
