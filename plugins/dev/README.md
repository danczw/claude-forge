# dev

| Type | Name | What it does |
|---|---|---|
| Skill | `commit` | Atomic commits with [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) messages |
| Skill | `issue` | Plan and implement GitHub issues on a fresh worktree, open a draft PR |
| Skill | `review-passes` | `/code-review`, `/security-review`, then a comment pass, each checked against the real diff |
| Skill | `premerge` | Required checks, conflicts, threads, reviews; lists open decisions before merge |
| Skill | `land` | Merge, then remove merged worktrees and branches |
| Skill | `issue-triage` | Fold into existing work or file an issue with existing labels and milestone |
| Agent | `code-reviewer` | Reviews a diff for bugs, security, simplicity and clarity |
| Command | `/dev:standup [since]` | Standup summary from your git log |
| Hook | `guard_bash.py` | Blocks `rm -rf /`, bare force-push, `mkfs`, `dd of=/dev/…`, `sleep` ≥ 30s, and `gh` when the repo owner is a logged-in gh account that isn't active |
