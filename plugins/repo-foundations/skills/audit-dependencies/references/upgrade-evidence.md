# Upgrade evidence

For each meaningful upgrade, gather:

1. Installed/resolved version from the lockfile or package-manager query.
2. Declared constraint and all workspace consumers.
3. Target version and publication metadata from the authoritative registry.
4. Supported runtime and peer dependency ranges.
5. Official changelog, release notes, migration guide, and current version-specific docs.
6. Repository usages of removed, renamed, or behavior-changing APIs.

Patch/minor classification still requires checking the project's compatibility policy; semantic-version labels are not proof. Major migrations should identify a rollback commit or lockfile restoration path, required data/config changes, and staged validation checkpoints.
