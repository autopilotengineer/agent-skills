# Stack signals

Inspect from the repository root and repeat at workspace/package boundaries.

| Concern | Strong evidence |
| --- | --- |
| Runtime | `.nvmrc`, `.node-version`, `.tool-versions`, `engines`, `global.json`, language toolchain files |
| Package manager | Lockfile plus manifest `packageManager`; treat multiple lockfiles as a conflict |
| Monorepo | Workspace declarations, package graph config, nested manifests, task-runner config |
| Framework | Declared dependency and framework configuration together; version comes from lockfile resolution |
| Validation | CI steps, documented commands, package scripts, test/lint/typecheck configs |
| Database | Schema/migration directories, ORM dependencies, compose services, connection variable names |
| Deployment | Workflow, container, infrastructure, or platform config; do not infer from a dependency alone |
| Environment | Checked-in examples, config loaders, schema validation, CI secret names, ignore rules |

For polyglot repositories, report each package's toolchain separately and identify which commands orchestrate the whole checkout.
