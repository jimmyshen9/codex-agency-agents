#!/usr/bin/env python3
"""Install generated Codex skills into ~/.codex/skills."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def detect_repo_root() -> Path:
    cwd = Path.cwd()
    if (cwd / "integrations").exists():
        return cwd
    return Path(__file__).resolve().parents[1]


def install(src_root: Path, dest_root: Path) -> int:
    src_root = src_root.resolve()
    dest_root = dest_root.resolve()
    if not src_root.exists():
        raise FileNotFoundError(f"Codex skills not found: {src_root}")
    dest_root.mkdir(parents=True, exist_ok=True)
    count = 0
    for skill_dir in sorted(p for p in src_root.iterdir() if p.is_dir()):
        target = dest_root / skill_dir.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(skill_dir, target)
        count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Codex skills into ~/.codex/skills.")
    parser.add_argument(
        "--src",
        type=Path,
        default=detect_repo_root() / "integrations" / "codex" / "skills",
        help="Source skills directory.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.home() / ".codex" / "skills",
        help="Destination Codex skills directory.",
    )
    args = parser.parse_args()

    count = install(args.src, args.dest)
    print(f"installed_codex_skills={count}")


if __name__ == "__main__":
    main()
