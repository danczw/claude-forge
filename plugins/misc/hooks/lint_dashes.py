#!/usr/bin/env python3
"""PostToolUse hook: flag em dashes Claude just wrote to a Markdown or text file.

Checks only the written text, not dashes already in the file. Exit code 2 shows stderr to Claude.
"""
import json
import sys

tool_input = json.load(sys.stdin).get("tool_input", {})
path = tool_input.get("file_path", "")
text = tool_input.get("content") or tool_input.get("new_string") or ""
if path.endswith((".md", ".txt")) and "—" in text:
    print(f"Em dash written to {path}: rewrite with a period, comma, colon or parentheses.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
