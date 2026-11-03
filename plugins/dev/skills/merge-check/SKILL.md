---
name: merge-check
description: Check whether a PR is ready to merge and list open decisions. Use when the user asks "ready to merge?", "any open decision before I merge?", or "anything left besides CI?".
---

# Merge check

Check, for the PR of the current branch or the one named:
- Required vs optional checks (`gh pr checks <pr> --required`); optional failures don't block.
- Behind base or conflicting (`gh pr view --json mergeable,mergeStateStatus`).
- Unresolved review threads and unanswered comments.
- Review passes ran on the current HEAD (see `run-reviews`).
- PR body matches what the branch now does; linked issues are correct.

Reply with a short numbered list of open decisions only, each with a recommendation. If none, say "ready" in one line. Then walk the decisions one by one with AskUserQuestion.
