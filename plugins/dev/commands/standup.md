---
description: Summarize my git activity for a standup update
argument-hint: "[since, e.g. '2 days ago']"
---

Run `git log --author="$(git config user.name)" --since="${ARGUMENTS:-yesterday}" --oneline --all` and summarize as **Done**, **In progress**, **Next**: ≤ 5 plain-language bullets, no hashes.
