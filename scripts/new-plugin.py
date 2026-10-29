#!/usr/bin/env python3
"""Scaffold a new plugin from templates/plugin and register it in marketplace.json.

Usage: scripts/new-plugin.py <name> "<description>" [--category <category>]
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "plugin"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("description")
parser.add_argument("--category", default="productivity")
args = parser.parse_args()

if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.name):
    sys.exit("Plugin name must be kebab-case, e.g. my-plugin")

dest = ROOT / "plugins" / args.name
if dest.exists():
    sys.exit(f"{dest} already exists")

shutil.copytree(TEMPLATE, dest)
for path in dest.rglob("*"):
    if path.is_file():
        text = path.read_text()
        text = text.replace("__PLUGIN_NAME__", args.name).replace("__DESCRIPTION__", args.description)
        path.write_text(text)

marketplace = json.loads(MARKETPLACE.read_text())
marketplace["plugins"].append({
    "name": args.name,
    "source": f"./plugins/{args.name}",
    "description": args.description,
    "version": "0.1.0",
    "category": args.category,
})
MARKETPLACE.write_text(json.dumps(marketplace, indent=2) + "\n")

print(f"Created plugins/{args.name} and registered it in marketplace.json")
print("Rename or delete the example-* files, then run: claude plugin validate .")
