---
name: commit
description: Commit changes as atomic commits with Conventional Commits 1.0.0 messages. Use when the user asks to commit, write a commit message, or split changes into commits.
---

# Commit

1. Read `git status` and `git diff HEAD`. Group changes into atomic commits: one logical change each, building and passing tests on its own, refactors/formatting separate from behaviour, tests and docs with their change. Split mixed files by hunk (write a patch, `git apply --cached`).
2. Show the plan (message + files per commit) and wait for approval.
3. Commit in order, then show `git log --oneline -n <count>`. Never push unless asked.

## Format ([Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/))
```
<type>[(scope)][!]: <description>

[body: why, not what; wrap at 72]

[footers: Token: value, e.g. Refs: #123]
```
- Types: `feat` (MINOR), `fix` (PATCH), `build`, `chore`, `ci`, `docs`, `perf`, `refactor`, `revert`, `style`, `test`.
- Header ≤ 72 chars, imperative, lowercase, no trailing period.
- Breaking change (MAJOR): `!` before the colon and/or a `BREAKING CHANGE: <migration>` footer.
