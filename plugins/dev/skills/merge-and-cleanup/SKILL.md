---
name: merge-and-cleanup
description: Merge a ready PR and clean up its worktree and branches. Use when the user says "merge", "merged, cleanup", "back to main and clean up", or asks to prune stale worktrees and branches.
---

# Merge and cleanup

1. If not merged yet: run `merge-check`, then merge with the repo's allowed method (`gh pr merge`) after the user approves.
2. From the main checkout: switch to the default branch, pull, `git fetch --prune`.
3. For each PR that is merged: remove its worktree (`git worktree remove`), delete the local and remote branch.
4. Never remove a worktree with uncommitted or unpushed work, or one another session is using; list those instead.
5. Close issues the PR resolved that are still open; close the milestone if it is done and the repo uses milestones per release.

Report what was removed and what was kept, in one short list.
