#!/usr/bin/env python3
"""PreToolUse hook: block gh / git push when the repo owner is a logged-in gh account that isn't active.

Exit code 2 blocks the tool call and shows stderr to Claude.
"""
import json
import re
import subprocess
import sys

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")
if "gh auth" in command or not re.search(r"(^|[;&|]\s*)gh\s|\bgit\s+push\b", command):
    sys.exit(0)


def run(*args):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=5, cwd=payload.get("cwd"))
        return r.stdout + r.stderr
    except (OSError, subprocess.TimeoutExpired):
        return ""


match = re.search(r"github\.com[:/]([^/]+)/", run("git", "remote", "get-url", "origin"))
if not match:
    sys.exit(0)
owner = match.group(1).lower()

active, accounts = None, set()
for account, flag in re.findall(r"account (\S+).*?Active account: (true|false)", run("gh", "auth", "status"), re.S):
    accounts.add(account.lower())
    if flag == "true":
        active = account.lower()

if owner in accounts and owner != active:
    print(f"Blocked by dev plugin guard: active gh account is {active}, repo owner is {owner}. "
          f"Run `gh auth switch -u {owner}` first, and switch back after if needed.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
