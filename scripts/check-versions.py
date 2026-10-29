#!/usr/bin/env python3
"""Fail if a plugin changed since <base> without a version bump, or if its
plugin.json and marketplace.json versions differ.

Usage: scripts/check-versions.py <base-ref>
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
base = sys.argv[1]


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


listed = {p["name"]: p["version"] for p in json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"]}
changed = {path.split("/")[1] for path in git("diff", "--name-only", f"{base}...HEAD").stdout.split() if path.startswith("plugins/")}
errors = []

for manifest in sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json")):
    name = manifest.parent.parent.name
    version = json.loads(manifest.read_text())["version"]
    if listed.get(name) != version:
        errors.append(f"{name}: plugin.json has {version}, marketplace.json has {listed.get(name)}")
    old = git("show", f"{base}:plugins/{name}/.claude-plugin/plugin.json")
    if name in changed and old.returncode == 0 and json.loads(old.stdout)["version"] == version:
        errors.append(f"{name}: changed but version is still {version}")

print("\n".join(errors) or "Plugin versions OK")
sys.exit(bool(errors))
