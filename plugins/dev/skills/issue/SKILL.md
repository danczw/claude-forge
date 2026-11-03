---
name: issue
description: Plan and implement one or more GitHub issues on a fresh worktree and open a PR. Use when the user says "plan implementation of issue #N", "work on #N", or names issues to tackle in one branch.
---

# Issue

1. Pull the default branch, then create a worktree and branch off it. Follow the repo's branch naming.
2. Read each issue's body, comments and linked issues/PRs (`gh issue view <n> --comments`). Check what already landed on the default branch.
3. Plan. Ask open questions with AskUserQuestion, recommended option first.
4. Commit with the `commit` skill; several issues get one commit each, or stacked PRs if the user asks.
5. Push and open a draft PR early that links the issues (`Closes #N`), metadata and body rules as in `issue-triage`.
6. Before marking ready, run the `review-passes` skill.

Ask before merging or force pushing.
