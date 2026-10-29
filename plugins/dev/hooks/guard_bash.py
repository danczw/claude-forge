#!/usr/bin/env python3
"""PreToolUse hook: block obviously destructive shell commands.

Exit code 2 blocks the tool call and shows stderr to Claude.
"""
import json
import re
import sys

BLOCKED = [
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+(/|~|\$HOME)(\s|$)", "recursive delete of / or home"),
    (r"\bgit\s+push\s+.*--force(?!-with-lease)", "force push (use --force-with-lease)"),
    (r"\bmkfs(\.\w+)?\b", "formatting a filesystem"),
    (r"\bdd\s+.*of=/dev/", "raw write to a device"),
]

payload = json.load(sys.stdin)
command = payload.get("tool_input", {}).get("command", "")

for pattern, reason in BLOCKED:
    if re.search(pattern, command):
        print(f"Blocked by dev plugin guard: {reason}", file=sys.stderr)
        sys.exit(2)

sys.exit(0)
