#!/usr/bin/env python3
"""Install Codex skills into ~/.codex/skills."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


BUNDLE_PATHS = {
    "full": Path("integrations") / "codex" / "skills",
    "engineering-codex": Path("integrations") / "codex" / "engineering-codex" / "skills",
    "ops-codex": Path("integrations") / "codex" / "ops-codex" / "skills",
}


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


def _normalize_bundle_names(bundle_names: list[str] | None) -> list[str]:
    ordered: list[str] = []
    for name in bundle_names or []:
        if name not in ordered:
            ordered.append(name)
    return ordered or ["engineering-codex"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Codex skills into ~/.codex/skills.")
    parser.add_argument(
        "--bundle",
        choices=sorted(BUNDLE_PATHS),
        action="append",
        default=None,
        help=(
            "Named Codex skill bundle to install. Can be specified multiple times. "
            "Ignored when --src is provided. Default: engineering-codex."
        ),
    )
    parser.add_argument(
        "--src",
        type=Path,
        default=None,
        help="Source skills directory.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=Path.home() / ".codex" / "skills",
        help="Destination Codex skills directory.",
    )
    args = parser.parse_args()

    if args.src is not None:
        count = install(args.src, args.dest)
        print(f"installed_codex_skills={count}")
        print(f"installed_codex_source={args.src}")
        return

    repo_root = detect_repo_root()
    bundles = _normalize_bundle_names(args.bundle)
    total = 0
    for bundle in bundles:
        total += install(repo_root / BUNDLE_PATHS[bundle], args.dest)
    print(f"installed_codex_skills={total}")
    print(f"installed_codex_bundles={','.join(bundles)}")


if __name__ == "__main__":
    main()
