#!/usr/bin/env python3
"""PreToolUse hook: block destructive shell commands, long sleeps, and gh calls on the wrong account.

Exit code 2 blocks the tool call and shows stderr to Claude.
"""
import json
import re
import subprocess
import sys

BLOCKED = [
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+(/|~|\$HOME)(\s|$)", "recursive delete of / or home"),
    (r"\bgit\s+push\s+.*--force(?!-with-lease)", "force push (use --force-with-lease)"),
    (r"\bmkfs(\.\w+)?\b", "formatting a filesystem"),
    (r"\bdd\s+.*of=/dev/", "raw write to a device"),
    (r"\bsleep\s+(([3-9]\d|\d{3,})(\.\d+)?s?|\d+(\.\d+)?[mhd])\b", "long sleep (wait with gh pr checks --watch, gh run watch or Monitor)"),
]

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")


def block(reason):
    print(f"Blocked by dev plugin guard: {reason}", file=sys.stderr)
    sys.exit(2)


def run(*args):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=5, cwd=payload.get("cwd"))
        return r.stdout + r.stderr
    except (OSError, subprocess.TimeoutExpired):
        return ""


for pattern, reason in BLOCKED:
    if re.search(pattern, command):
        block(reason)

# gh uses the active account; block when the repo owner is another logged-in account.
gh_calls = re.findall(r"(?<![\w./-])gh\s+(\w+)", command)
if gh_calls and set(gh_calls) != {"auth"}:
    owner = re.search(r"github\.com[:/]([^/]+)/", run("git", "remote", "get-url", "origin"))
    status = run("gh", "auth", "status")
    accounts = {a.lower(): f == "true" for a, f in re.findall(r"account (\S+).*?Active account: (true|false)", status, re.S)}
    owner = owner and owner.group(1).lower()
    if owner in accounts and not accounts[owner]:
        block(f"repo owner {owner} is not the active gh account. Run `gh auth switch -u {owner}` first.")

sys.exit(0)
