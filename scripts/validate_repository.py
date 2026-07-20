#!/usr/bin/env python3
"""Deterministically validate the Autopilot Engineer Agent Skills repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "pr-workflow": {
        "start-feature",
        "checkpoint-work",
        "review-changes",
        "submit-pull-request",
        "address-review-comments",
        "resolve-git-conflicts",
        "fix-pr-checks",
        "sync-with-base",
    },
    "repo-foundations": {
        "repo-doctor",
        "write-agent-context",
        "bootstrap-quality",
        "audit-dependencies",
        "protect-secrets",
        "recommend-mcp-servers",
        "prepare-first-release",
    },
    "typescript-web": {
        "audit-nextjs-project",
        "audit-nestjs-project",
        "modernize-typescript-project",
        "verify-framework-change",
        "bootstrap-typescript-service",
    },
}
LIFECYCLE = (
    "## Current state",
    "## Intended action",
    "## Execution",
    "## Validation",
    "## Result",
    "## Next action",
)
REQUIRED_SCENARIOS = {
    "dirty-working-tree",
    "non-main-default-branch",
    "detached-head",
    "invalid-github-auth",
    "no-pr-for-branch",
    "outdated-review-comment",
    "conflicting-review-requests",
    "failing-tests-after-fix",
    "merge-conflict",
    "rebase-conflict",
    "monorepo-package-detection",
    "nextjs-app-router",
    "nextjs-pages-router",
    "nestjs-missing-validation-config",
    "dependency-peer-conflict",
    "dependency-major-migration",
    "mcp-none-needed",
}
STOPWORDS = {
    "a", "an", "and", "for", "from", "in", "into", "of", "on", "or", "the",
    "to", "use", "when", "with", "asked", "developer", "project", "repository",
    "existing", "without", "safe", "safely",
}


class Checks:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def check(self, condition: bool, label: str, detail: str = "") -> None:
        if condition:
            print(f"PASS {label}")
            return
        message = f"{label}: {detail}" if detail else label
        self.failures.append(message)
        print(f"FAIL {message}")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing frontmatter delimiter")
    metadata: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip():
            continue
        if raw.startswith((" ", "\t")) or ":" not in raw:
            raise ValueError(f"unsupported frontmatter syntax: {raw!r}")
        key, value = raw.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, text[end + 5 :]


def tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", value.lower())
        if len(token) > 2 and token not in STOPWORDS
    }


def text_files() -> list[Path]:
    allowed = {".md", ".json", ".yaml", ".yml", ".py", ".txt"}
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and path.suffix.lower() in allowed
    )


def main() -> int:
    checks = Checks()
    print("PROGRESS discovering skills", file=sys.stderr)

    skill_paths = sorted(ROOT.glob("plugins/*/skills/*/SKILL.md"))
    checks.check(len(skill_paths) == 20, "skill count", f"found {len(skill_paths)}, expected 20")

    discovered: dict[str, set[str]] = {}
    names: list[str] = []
    descriptions: dict[str, str] = {}
    for path in skill_paths:
        pack = path.parents[2].name
        folder = path.parent.name
        discovered.setdefault(pack, set()).add(folder)
        try:
            metadata, body = parse_frontmatter(path)
        except ValueError as error:
            checks.check(False, f"frontmatter {path.relative_to(ROOT)}", str(error))
            continue

        checks.check(set(metadata) == {"name", "description"}, f"frontmatter keys {folder}", str(sorted(metadata)))
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        names.append(name)
        descriptions[name] = description
        checks.check(name == folder, f"folder matches name {folder}", f"frontmatter name is {name!r}")
        checks.check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)), f"valid name {folder}")
        checks.check(0 < len(description) <= 1024, f"description length {folder}", str(len(description)))
        checks.check(len(path.read_text(encoding="utf-8").splitlines()) < 500, f"line limit {folder}")

        positions = [body.find(heading) for heading in LIFECYCLE]
        checks.check(all(position >= 0 for position in positions), f"lifecycle headings {folder}")
        checks.check(positions == sorted(positions), f"lifecycle order {folder}", str(positions))

        refs = set(re.findall(r"references/[A-Za-z0-9._/-]+", body))
        missing_refs = sorted(ref for ref in refs if not (path.parent / ref).is_file())
        checks.check(not missing_refs, f"references exist {folder}", ", ".join(missing_refs))
        checks.check((path.parent / "agents/openai.yaml").is_file(), f"OpenAI metadata {folder}")
        forbidden_docs = [name for name in ("README.md", "CHANGELOG.md", "INSTALLATION.md") if (path.parent / name).exists()]
        checks.check(not forbidden_docs, f"no extra skill docs {folder}", ", ".join(forbidden_docs))

    checks.check(discovered == EXPECTED, "canonical pack catalog", f"discovered {discovered}")
    checks.check(len(names) == len(set(names)), "unique skill names")

    overlap: list[str] = []
    desc_items = sorted(descriptions.items())
    for index, (left_name, left_desc) in enumerate(desc_items):
        left_tokens = tokens(left_desc)
        for right_name, right_desc in desc_items[index + 1 :]:
            right_tokens = tokens(right_desc)
            union = left_tokens | right_tokens
            similarity = len(left_tokens & right_tokens) / len(union) if union else 0
            if similarity >= 0.60:
                overlap.append(f"{left_name}/{right_name}={similarity:.2f}")
    checks.check(not overlap, "trigger descriptions are distinct", ", ".join(overlap))

    print("PROGRESS validating manifests and documentation", file=sys.stderr)
    json_paths = [ROOT / ".claude-plugin/marketplace.json", *sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json"))]
    parsed_json: dict[Path, object] = {}
    for path in json_paths:
        try:
            parsed_json[path] = json.loads(path.read_text(encoding="utf-8"))
            checks.check(True, f"JSON parses {path.relative_to(ROOT)}")
        except (OSError, json.JSONDecodeError) as error:
            checks.check(False, f"JSON parses {path.relative_to(ROOT)}", str(error))

    marketplace = parsed_json.get(ROOT / ".claude-plugin/marketplace.json", {})
    marketplace_names = {
        item.get("name") for item in marketplace.get("plugins", [])
    } if isinstance(marketplace, dict) else set()
    checks.check(marketplace_names == set(EXPECTED), "marketplace pack catalog", str(marketplace_names))

    required_root = {
        "README.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE", "AGENTS.md",
        "scripts/validate_repository.py", ".github/workflows/validate.yml",
    }
    missing_root = sorted(path for path in required_root if not (ROOT / path).is_file())
    checks.check(not missing_root, "required repository files", ", ".join(missing_root))

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme_markers = (
        "/plugin marketplace add autopilotengineer/agent-skills",
        "gh skill preview autopilotengineer/agent-skills",
        "--agent codex",
        "--agent claude-code",
        "--agent github-copilot",
        "--agent cursor",
        "<repo>/.agents/skills/",
        "<repo>/.claude/skills/",
        "Inspect before installing",
    )
    checks.check(all(marker in readme for marker in readme_markers), "cross-agent installation docs")
    checks.check("Apache License" in (ROOT / "LICENSE").read_text(encoding="utf-8"), "Apache-2.0 license text")

    print("PROGRESS validating scenarios", file=sys.stderr)
    scenario_ids: set[str] = set()
    for path in sorted((ROOT / "evals/scenarios").glob("*.json")):
        try:
            scenario = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            checks.check(False, f"scenario parses {path.name}", str(error))
            continue
        required_keys = {"id", "skill", "prompt", "fixture", "expected", "forbidden"}
        checks.check(required_keys <= set(scenario), f"scenario schema {path.name}")
        scenario_ids.add(scenario.get("id", ""))
        checks.check(scenario.get("skill") in set(names), f"scenario skill {path.name}", str(scenario.get("skill")))
        checks.check(bool(scenario.get("expected")), f"scenario expectations {path.name}")
        checks.check(bool(scenario.get("forbidden")), f"scenario guardrails {path.name}")
    missing_scenarios = sorted(REQUIRED_SCENARIOS - scenario_ids)
    checks.check(not missing_scenarios, "required scenario coverage", ", ".join(missing_scenarios))

    print("PROGRESS scanning repository content", file=sys.stderr)
    scaffold_tokens = ("TO" + "DO", "T" + "BD", "FIX" + "ME", "REPLACE" + "_ME")
    scaffold_hits: list[str] = []
    absolute_hits: list[str] = []
    secret_hits: list[str] = []
    user_path_patterns = (
        re.compile(r"/" + "Users" + r"/[^/\s]+/"),
        re.compile(r"/" + "home" + r"/[^/\s]+/"),
        re.compile(r"[A-Za-z]:\\" + "Users" + r"\\[^\\\s]+\\"),
    )
    secret_patterns = (
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"AKIA[A-Z0-9]{16}"),
        re.compile(r"ghp_[A-Za-z0-9]{20,}"),
        re.compile(r"sk-[A-Za-z0-9]{20,}"),
    )
    for path in text_files():
        content = path.read_text(encoding="utf-8")
        relative = str(path.relative_to(ROOT))
        if any(token in content for token in scaffold_tokens):
            scaffold_hits.append(relative)
        if any(pattern.search(content) for pattern in user_path_patterns):
            absolute_hits.append(relative)
        if any(pattern.search(content) for pattern in secret_patterns):
            secret_hits.append(relative)
    checks.check(not scaffold_hits, "no authoring scaffolds", ", ".join(scaffold_hits))
    checks.check(not absolute_hits, "no user-specific absolute paths", ", ".join(absolute_hits))
    checks.check(not secret_hits, "no likely secrets", ", ".join(secret_hits))

    if checks.failures:
        print(f"RESULT FAIL ({len(checks.failures)} checks failed)")
        for failure in checks.failures:
            print(f" - {failure}")
        return 1

    print("RESULT PASS (repository is ready for publication checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
