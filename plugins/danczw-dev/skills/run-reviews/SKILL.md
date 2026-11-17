---
name: run-reviews
description: Run code review, security review and a comment pass on the current branch in order, fixing between passes. Use before opening or readying a PR, or when the user asks to "run the reviews" or whether the reviews ran.
---

# Run reviews

Order, fixing what each reports before the next (follow the repo's CLAUDE.md if it defines its own):
1. `/code-review`: correctness first, so bugs don't show up as phantom security findings.
2. `/security-review`.
3. Comment pass: read every comment the branch added or touched; cut ones that restate the code, narrate, or hold history git already has. Keep why-comments: ordering constraints, required flags, origins of magic values.

Skip 1–2 for docs-only branches. Run each pass from the worktree holding the branch, and check the diff it read matches `git diff --stat origin/<base>...HEAD` (three dots). An empty or stale diff is not a pass. Commit fixes atomically and list the passes that ran, at which SHA, in the PR body.
