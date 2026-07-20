# Baseline choices

Choose tools from existing dependencies first. A minimum baseline usually exposes separate commands for:

- formatting check, with formatting write as a distinct developer command
- linting for likely defects
- static type checking when the language supports it
- focused unit tests
- build or package verification
- a CI aggregate that runs on pull requests

For monorepos, prefer the existing task graph and affected-package mechanisms while retaining a documented full-check command. Pin action versions and grant only required workflow permissions. Avoid broad auto-fix steps in CI because CI should diagnose drift, not rewrite contributor branches.
