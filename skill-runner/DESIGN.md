# Skill Runner - Design Document

## Problem Statement

Claude Code skills (`.claude/skills/<name>/SKILL.md`) only load in interactive sessions within a project directory. They cannot be invoked programmatically via `claude -p` or from the shell. This creates a gap where:

1. Shell scripts calling `claude -p` cannot use skills
2. Mentioning "use the X skill" in a prompt does nothing - skills aren't loaded
3. Skills become dead code outside of interactive Claude Code sessions

### Original Use Case: `gcam` (git commit with AI message)

A shell function that:
1. Stages all changes (`git add -A`)
2. Gets the diff
3. Calls Claude to generate a conventional commit message
4. Opens editor for review
5. Commits

The original implementation piped the diff to `claude -p` with a prompt mentioning "use the commit-messager skill" - but the skill was never actually loaded.

## Analysis of Approaches

| Approach | Shell CLI | Claude Code REPL | Token Efficiency | Complexity |
|----------|-----------|------------------|------------------|------------|
| `claude -p --system-prompt "$(cat skill)"` | ✓ | ✗ | Medium | Low |
| `claude -p` with inline prompt | ✓ | ✗ | High | Low |
| Skill file in `.claude/skills/` | ✗ | ✓ (if in project) | High | Low |
| Claude Agent SDK (`claude-agent-sdk`) | ✓ | ✗ | High | Medium |
| MCP Server tool | ✓ | ✓ | High | High |

### Key Insight

Skills are essentially prompt templates with metadata. The value is in:
- Reusable, versioned prompt engineering
- Declarative input definitions
- Separation of data gathering from inference

Rather than building a single-purpose commit message tool, we can build a **generalized skill runner** that executes any skill by reference.

## Requirements

### Functional Requirements

1. **Execute skills by name**: `skill run <name>`
2. **Auto-gather inputs**: Skills define shell commands to gather inputs (e.g., `git diff --cached`)
3. **Accept explicit inputs**: Override auto-gathering with `--input key=value`
4. **Support stdin**: Pipe input for single-input skills
5. **List available skills**: `skill list`
6. **Show skill details**: `skill show <name>`
7. **Work from any directory**: Find skills in standard locations

### Non-Functional Requirements

1. **Separation of concerns**: Data gathering (deterministic) vs inference (LLM)
2. **Token efficiency**: Don't waste tokens on deterministic operations
3. **Portable**: Works in shell, Claude Code REPL (via `!`), and as MCP tool
4. **Simple skill authoring**: Markdown with YAML frontmatter
5. **No redundancy**: Single source of truth for skill definitions

### Skill Discovery Paths

1. `./.claude/skills/<name>/SKILL.md` (project-local)
2. `~/.claude/skills/<name>/SKILL.md` (user global)

## Design Decisions

### 1. Skill Schema: YAML Frontmatter + Markdown

```yaml
---
name: commit-messager
description: Generate conventional commit messages from git diffs
inputs:
  diff:
    command: git diff --cached
    description: Staged git changes
    required: true
output:
  format: text
---

The prompt template goes here.

Use {{input_name}} for placeholder substitution.
```

**Rationale**:
- Familiar format (like Jekyll/Hugo frontmatter)
- Easy to author and edit
- Structured metadata + freeform prompt
- Parseable with standard YAML libraries

### 2. Input Resolution Strategy

```
For each input defined in skill:
  If provided via --input or MCP argument:
    Use provided value
  Else if input has a command:
    Execute command to auto-gather
  Else if required:
    Raise error
```

**Rationale**:
- Deterministic operations stay deterministic (no LLM needed for `git diff`)
- Flexibility: can override any input
- Self-documenting: skill declares what it needs

### 3. Single-File Scripts with UV Shebang

```python
#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["claude-agent-sdk", "typer", "rich", ...]
# ///
```

**Rationale**:
- Zero installation required
- Dependencies managed inline
- Portable across machines
- Matches user's existing tooling preferences

### 4. Dual Distribution: CLI + MCP Server

**CLI (`skill`)**: For shell usage and `!skill run X` from Claude Code
**MCP Server (`skill-mcp`)**: Native Claude Code tool integration

**Rationale**:
- CLI is immediate, works everywhere
- MCP enables seamless integration without `!` escape
- Same core logic, different interfaces

### 5. Claude Agent SDK

Uses `claude-agent-sdk` (PyPI) for Claude Code CLI integration. This SDK handles the streaming protocol, message parsing, and authentication via the user's Claude Code subscription.

**Rationale**:
- Direct integration with Claude Code CLI
- Subscription auth (no API key needed)
- Handles streaming message protocol

## Architecture

```
skill-runner/
├── skill                  # Standalone CLI (uv shebang)
├── skill-mcp              # Standalone MCP server (uv shebang)
├── pyproject.toml         # For package installation
└── src/skill_runner/      # Package version
    ├── __init__.py
    ├── schema.py          # Skill model, parsing, discovery
    ├── core.py            # SkillRunner class
    ├── cli.py             # Typer CLI
    └── mcp_server.py      # MCP server
```

### Data Flow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   CLI/MCP   │────▶│ SkillRunner  │────▶│  Anthropic  │
│   Request   │     │              │     │ Claude Code │
│     CLI     │
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ Input        │
                    │ Resolution   │
                    │              │
                    │ - provided?  │
                    │ - command?   │
                    │ - required?  │
                    └──────────────┘
```

### Execution Contexts

| Context | Command | Data Gathering | Inference |
|---------|---------|----------------|-----------|
| Shell | `skill run commit-messager` | Runner executes `git diff --cached` | Runner calls LLM |
| Shell (explicit) | `skill run commit-messager -i diff="..."` | User provided | Runner calls LLM |
| Shell (piped) | `git diff \| skill run commit-messager` | Stdin mapped to single input | Runner calls LLM |
| Claude Code (`!`) | `!skill run commit-messager` | Runner executes command | Runner calls LLM |
| MCP tool | `run_skill("commit-messager")` | Runner executes command | Runner calls LLM |
| MCP tool (with input) | `run_skill("commit-messager", inputs={...})` | Claude gathered, passed in | Runner calls LLM |

## Usage Examples

### CLI

```bash
# Auto-gather inputs via skill-defined commands
skill run commit-messager

# Explicit input
skill run commit-messager --input diff="$(git diff HEAD~1)"

# Piped input (single-input skills)
git diff | skill run commit-messager

# List available skills
skill list -v

# Show skill details
skill show commit-messager
```

### MCP Server Configuration

Add to `~/.claude/settings.json` or project `.claude/settings.local.json`:

```json
{
  "mcpServers": {
    "skill-runner": {
      "command": "/path/to/skill-runner/skill-mcp"
    }
  }
}
```

Then in Claude Code, the `run_skill` tool becomes available natively.

### Shell Integration (`gcam`)

```bash
gcam() {
  git add -A
  [[ -z "$(git diff --cached)" ]] && echo "No changes" && return 1

  local msg
  msg="$(skill run commit-messager)" || return 1

  # Open in editor for review, then commit
  ...
}
```

## Future Considerations

1. **Skill chaining**: Output of one skill as input to another
2. **Skill parameters**: Runtime configuration beyond inputs
3. **Skill versioning**: Lock to specific skill versions
4. **Remote skills**: Fetch skills from URLs/repos
5. **Skill testing**: Validate skills against example inputs/outputs
