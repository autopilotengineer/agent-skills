# Validation discovery

Use repository evidence in this order:

1. `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and the README.
2. CI workflow commands and reusable scripts.
3. Package-manager scripts and lockfile-selected tooling.
4. Language-native manifests and test configuration.
5. Changed-package metadata in a monorepo.

Run the narrowest relevant checks before broader ones. Typical categories are formatting, linting, type checking, unit tests, integration tests, build, and generated-file consistency. Do not invent a command or install a different package manager. If a check cannot run, record `SKIP` with the exact reason and remaining risk.
