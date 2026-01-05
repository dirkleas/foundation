# Skill Runner

Execute Claude skills from CLI or MCP server.

## Quick Start

```bash
# List available skills
./skill list

# Show skill details
./skill show commit-messager

# Run a skill (auto-gathers inputs)
./skill run commit-messager

# Run with explicit input
./skill run commit-messager --input diff="$(git diff)"

# Pipe input (single-input skills)
git diff | ./skill run commit-messager
```

## Installation

No installation required - uses uv shebang for dependency management.

Or install as package:

```bash
uv pip install -e .
```

## Skill Locations

Skills are discovered from:

1. `./.claude/skills/<name>/SKILL.md` (project)
2. `~/.claude/skills/<name>/SKILL.md` (global)

## Skill Format

```yaml
---
name: my-skill
description: What this skill does
inputs:
  input_name:
    command: shell command to auto-gather
    description: What this input is
    required: true
output:
  format: text
---

Your prompt template here.

Use {{input_name}} placeholders for inputs.
```

## MCP Server

Add to Claude Code settings:

```json
{
  "mcpServers": {
    "skill-runner": {
      "command": "/path/to/skill-runner/skill-mcp"
    }
  }
}
```

Available tools:
- `run_skill(skill_name, inputs?)` - Execute a skill
- `list_skills()` - List available skills
- `show_skill(skill_name)` - Show skill details

## CLI Reference

```
skill run <name> [--input key=value]...  Run a skill
skill list [-v]                          List skills
skill show <name>                        Show skill details
```

## See Also

- [DESIGN.md](DESIGN.md) - Architecture and design decisions
