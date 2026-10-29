# claude-forge

Personal Claude Code plugin marketplace named `forge`.

**Less is more.** Keep skills, agents, hooks and scripts to the fewest words and simplest code that keep the essentials, and answer briefly. Less code is more.

- New plugins: run `scripts/new-plugin.py <name> "<description>"`. Don't hand-copy the template.
- Every plugin under `plugins/` must have an entry in `.claude-plugin/marketplace.json`.
- When changing a plugin, bump its `version` in both `plugin.json` and `marketplace.json`.
- Skill `description` fields decide when a skill triggers: state what it does and "Use when ...".
- Hook commands reference files with `${CLAUDE_PLUGIN_ROOT}`, never absolute paths.
- Validate with `claude plugin validate .` before committing.
