#!/usr/bin/env python3
"""Check or apply the Project-Wisdom DerpFest 17 patch set to a clean repo tree."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def run(*args, cwd):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    parser.add_argument("root", type=Path, help="Android repo checkout root")
    parser.add_argument("--project", action="append", help="limit to one project; repeatable")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    manifest = json.loads((here / "manifest.json").read_text())
    rows = manifest["patches"]
    if args.project:
        unknown = set(args.project) - {x["project"] for x in rows}
        if unknown:
            parser.error("unknown project(s): " + ", ".join(sorted(unknown)))
        rows = [x for x in rows if x["project"] in args.project]
    failures = []
    for row in rows:
        repo = args.root.resolve() / row["project"]
        patch = here / row["patch"]
        if hashlib.sha256(patch.read_bytes()).hexdigest() != row["sha256"]:
            failures.append(f"{row['project']}: patch checksum mismatch")
            continue
        head = run("git", "rev-parse", "HEAD", cwd=repo)
        if head.returncode or head.stdout.strip() != row["base_commit"]:
            failures.append(f"{row['project']}: expected HEAD {row['base_commit']}, found {head.stdout.strip() or head.stderr.strip()}")
            continue
        status = run("git", "status", "--porcelain=v1", "-uall", cwd=repo)
        if status.returncode or status.stdout.strip():
            failures.append(f"{row['project']}: worktree must be clean")
            continue
        check = run("git", "apply", "--check", str(patch), cwd=repo)
        if check.returncode:
            failures.append(f"{row['project']}: {check.stderr.strip()}")
            continue
        print(f"OK {row['project']}: {row['files']} files")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    if args.apply:
        for row in rows:
            repo = args.root.resolve() / row["project"]
            result = run("git", "apply", str(here / row["patch"]), cwd=repo)
            if result.returncode:
                print(f"FAILED {row['project']}: {result.stderr.strip()}", file=sys.stderr)
                return 1
            print(f"APPLIED {row['project']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
