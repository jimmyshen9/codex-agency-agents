#!/usr/bin/env python3
"""Generate Codex skills from Agency agent markdown files."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


AGENT_DIRS = [
    "design",
    "engineering",
    "game-development",
    "marketing",
    "paid-media",
    "product",
    "project-management",
    "testing",
    "support",
    "spatial-computing",
    "specialized",
]


FRONTMATTER_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", re.DOTALL)


def detect_repo_root() -> Path:
    cwd = Path.cwd()
    if (cwd / "integrations").exists() and (cwd / "engineering").exists():
        return cwd
    return Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def parse_agent(path: Path) -> tuple[str, str, str] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    frontmatter, body = match.groups()
    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ": " not in line:
            continue
        key, value = line.split(": ", 1)
        fields[key.strip()] = value.strip()
    name = fields.get("name")
    description = fields.get("description")
    if not name or not description:
        return None
    return name, description, body


def build_skill_text(name: str, description: str, body: str) -> str:
    description = description.rstrip().rstrip(".")
    slug = f"agency-{slugify(name)}"
    return (
        "---\n"
        f"name: {slug}\n"
        f"description: {description}. Use when Codex should adopt the {name} specialist role from The Agency for tasks in this domain.\n"
        "---\n"
        f"# {name}\n\n"
        f"Adopt the {name} role and follow the persona, operating rules, deliverables, and workflows below.\n\n"
        f"{body}"
    )


def convert(repo_root: Path, out_root: Path) -> int:
    skills_root = out_root / "skills"
    if skills_root.exists():
        shutil.rmtree(skills_root)
    skills_root.mkdir(parents=True, exist_ok=True)

    count = 0
    for directory in AGENT_DIRS:
        dir_path = repo_root / directory
        if not dir_path.exists():
            continue
        for path in sorted(dir_path.rglob("*.md")):
            parsed = parse_agent(path)
            if not parsed:
                continue
            name, description, body = parsed
            slug = f"agency-{slugify(name)}"
            skill_dir = skills_root / slug
            skill_dir.mkdir(parents=True, exist_ok=True)
            (skill_dir / "SKILL.md").write_text(
                build_skill_text(name, description, body),
                encoding="utf-8",
            )
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Codex skills from Agency agents.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=detect_repo_root(),
        help="Path to the repository root.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=detect_repo_root() / "integrations" / "codex",
        help="Output directory for Codex integration files.",
    )
    args = parser.parse_args()

    count = convert(args.repo_root, args.out)
    print(f"generated_codex_skills={count}")


if __name__ == "__main__":
    main()
