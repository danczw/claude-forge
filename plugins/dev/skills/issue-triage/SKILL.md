---
name: issue-triage
description: Decide whether a finding or follow-up folds into existing work or becomes a new GitHub issue, and file it with labels and milestone. Use when the user asks "can this be folded into an existing issue?", "file it as an issue", or to label, size or milestone issues.
---

# Issue triage

1. Search open issues and PRs (`gh issue list --search`, `gh pr list`) for one that already covers it. Prefer folding into in-flight work or an existing issue (edit its body or comment) over filing a new one.
2. Otherwise draft the issue: title, short problem, evidence (file:line, links), done-when. Use only existing labels (`gh label list`) and milestones, plus the repo's assignee convention.
3. Show the draft and ask before `gh issue create`.

Sizing on request: xs–xl by scope and risk, one line of reason each. Never hard-wrap GitHub bodies: one paragraph per line.
