# claude-forge

My personal [Claude Code](https://docs.claude.com/en/docs/claude-code) plugin marketplace: skills, agents, commands and hooks, versioned in one repo.

## Install

```bash
# from GitHub
/plugin marketplace add <github-user>/claude-forge
# or from a local clone while developing
/plugin marketplace add ~/code/claude-forge

/plugin install dev@forge
```

Update after pushing changes: `/plugin marketplace update forge`

## Plugins

| Plugin | Description |
|---|---|
| [dev](plugins/dev) | Commit messages, code review agent, standup command, dangerous-command guard |

## Add a plugin

```bash
scripts/new-plugin.py my-plugin "What it does" --category productivity
claude plugin validate .
```

Bump `version` in both `plugin.json` and `marketplace.json` when you change a plugin, otherwise installed copies won't update.
