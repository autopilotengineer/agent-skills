# Autopilot Engineer Agent Skills

**Senior-principal guardrails for shipping AI-assisted software safely.**

Go from idea to reviewed PR without skipping the engineering.

This repository packages portable [Agent Skills](https://agentskills.io)—small folders with a `SKILL.md`, optional references, and optional scripts that compatible coding agents load when a task matches. The packs are written for newer developers and people building through AI-assisted or “vibe coding” workflows who still want safe Git practices, evidence-backed reviews, current documentation, reproducible validation, and human approval before consequential actions.

## Why these skills exist

Fast code generation does not remove the need to understand the current repository, protect local work, verify version-specific behavior, run the right checks, or review a pull request. These skills make those engineering gates visible:

> Current state → Intended action → Execution → Validation → Result → Next action

Every skill inspects before editing, preserves unrelated work, reports failures honestly, avoids exposing secrets, and keeps difficult-to-reverse external actions behind explicit authority.

## Packs

### PR Workflow

| Skill | Use it for |
| --- | --- |
| `start-feature` | Start a focused branch from the repository's real default branch. |
| `checkpoint-work` | Review, validate, stage, and Conventional-Commit one coherent change. |
| `review-changes` | Review the correct merge-base diff without implementing fixes. |
| `submit-pull-request` | Validate, push, and open a detailed draft PR. |
| `address-review-comments` | Triage, fix, verify, reply to, and resolve review feedback safely. |
| `resolve-git-conflicts` | Resolve merge, rebase, cherry-pick, revert, or stash conflicts semantically. |
| `fix-pr-checks` | Diagnose the first actionable GitHub Actions failure and make the smallest fix. |
| `sync-with-base` | Update a branch from its verified base using an informed merge or rebase. |

### Repo Foundations

| Skill | Use it for |
| --- | --- |
| `repo-doctor` | Produce a read-only, prioritized repository health report. |
| `write-agent-context` | Create concise evidence-based `AGENTS.md` or `CLAUDE.md` guidance. |
| `bootstrap-quality` | Add the smallest useful formatting, lint, types, tests, and CI baseline. |
| `audit-dependencies` | Investigate and incrementally upgrade dependencies with migration evidence. |
| `protect-secrets` | Audit and improve ignore, environment, logging, CI, and exposure handling. |
| `recommend-mcp-servers` | Recommend only justified, least-privilege MCP servers—or none. |
| `prepare-first-release` | Assess packaging, documentation, security, and reproducible release readiness. |

### TypeScript Web

| Skill | Use it for |
| --- | --- |
| `audit-nextjs-project` | Audit the detected Next.js version and App/Pages Router architecture. |
| `audit-nestjs-project` | Audit NestJS modules, request safety, auth, persistence, and operations. |
| `modernize-typescript-project` | Plan and apply incremental TypeScript modernization without breaking consumers. |
| `verify-framework-change` | Verify a proposed library/framework change against official versioned sources. |
| `bootstrap-typescript-service` | Establish a practical production-shaped TypeScript service baseline. |

## Inspect before installing

Skills can instruct an agent to read files, run commands, change code, or call external tools. Review a skill's `SKILL.md` and bundled files before installation, confirm that its permissions match your environment, and keep normal host approval prompts enabled.

List the available skills without installing them:

```bash
npx skills add autopilotengineer/agent-skills --list
```

Review the selected skill's `SKILL.md`, `agents/`, and `references/` files in this repository before continuing.

## Install with the skills CLI (recommended)

The open ecosystem's `skills` CLI is the primary cross-agent installation path. It requires Node.js and npm, runs through `npx` without a permanent CLI installation, detects supported coding agents, and lets you choose skills and destinations interactively:

```bash
npx skills add autopilotengineer/agent-skills
```

Install one skill globally for a specific agent:

```bash
npx skills add autopilotengineer/agent-skills \
  --skill start-feature \
  --agent codex \
  --global
```

Install every skill globally for selected agents without prompts:

```bash
npx skills add autopilotengineer/agent-skills \
  --skill '*' \
  --agent codex \
  --agent claude-code \
  --global \
  --yes
```

Check installed skills and apply updates:

```bash
npx skills list
npx skills update
```

The `skills` CLI collects anonymous installation telemetry by default to power ecosystem rankings. Opt out for a command by setting `DISABLE_TELEMETRY=1`.

## Install with Claude Code marketplace

Inside Claude Code:

```text
/plugin marketplace add autopilotengineer/agent-skills
/plugin install pr-workflow@autopilot-engineer-skills
/plugin install repo-foundations@autopilot-engineer-skills
/plugin install typescript-web@autopilot-engineer-skills
```

Refresh later with:

```text
/plugin marketplace update autopilot-engineer-skills
```

Claude plugin skills are namespaced, for example `/pr-workflow:start-feature`.

## Alternative: Install with GitHub CLI

GitHub CLI's preview `gh skill` commands provide a GitHub-native alternative, including remote preview, version pinning, source-tracked installs, and publication validation.

Preview a skill:

```bash
gh skill preview autopilotengineer/agent-skills start-feature
```

Install all skills for one host at project scope (the default) or user scope:

```bash
gh skill install autopilotengineer/agent-skills --all --agent codex --scope user
gh skill install autopilotengineer/agent-skills --all --agent claude-code --scope user
gh skill install autopilotengineer/agent-skills --all --agent github-copilot --scope user
gh skill install autopilotengineer/agent-skills --all --agent cursor --scope user
```

Install one skill instead:

```bash
gh skill install autopilotengineer/agent-skills checkpoint-work --agent codex --scope user
```

Check for updates without changing files, then apply updates when ready:

```bash
gh skill update --dry-run
gh skill update --all
```

## Manual installation fallback

Clone the repository, inspect the selected folder, then copy the complete skill directory—including `agents/` and `references/`—into a directory your host scans.

Portable project/user locations include:

- Codex: `<repo>/.agents/skills/` or `$HOME/.agents/skills/`
- GitHub Copilot: `<repo>/.agents/skills/` or `$HOME/.agents/skills/`
- Claude Code: `<repo>/.claude/skills/` or `$HOME/.claude/skills/`

For Cursor and other hosts, prefer `npx skills add ... --agent <host>` so the current skills CLI selects the host-specific path. Example manual copy for a shared project skill:

```bash
git clone https://github.com/autopilotengineer/agent-skills.git
mkdir -p /path/to/your-project/.agents/skills
cp -R agent-skills/plugins/pr-workflow/skills/start-feature /path/to/your-project/.agents/skills/
```

Restart or reload the host if it does not detect a newly created top-level skills directory.

## Example requests

- “I have changes in this folder, but I want to start a new login feature without losing anything.”
- “Save only the API fix. The screenshots and generated files are unrelated.”
- “Review this branch for bugs and missing tests, but don't change the code.”
- “Open a draft PR and include exact steps my teammate can use to test it.”
- “Two reviewers asked for conflicting things. Help me classify the comments before editing.”
- “This repo is new to me. Tell me what stack it uses and the highest-risk missing safeguards.”
- “Is upgrading this Next.js project to the target major safe? Verify it against official docs.”
- “Recommend MCP servers for this repository, including the option that it needs none.”

Explicitly invoke a skill using the syntax your host supports, such as `$repo-doctor`, `/repo-doctor`, or a Claude plugin namespace.

## Contributing and testing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing a skill. New skills must be initialized with the `skill-creator` tooling and remain portable open-format skills.

Run the deterministic repository checks:

```bash
python3 scripts/validate_repository.py
```

Before publishing, also validate every changed skill with `quick_validate.py`, validate the Claude marketplace when Claude Code is installed, and run GitHub CLI's publication dry run:

```bash
claude plugin validate .
gh skill publish --dry-run
```

Scenario fixtures live in [`evals/scenarios`](evals/scenarios). Contributions should add or update scenarios for changed behavior, especially failure and permission boundaries.

## License

Apache-2.0. See [LICENSE](LICENSE).
