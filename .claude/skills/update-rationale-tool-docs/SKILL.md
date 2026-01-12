---
name: update-rationale-tool-docs
description: Update README.md rationale section with documentation for brew-installed tools
---

Update the README.md rationale section to document brew-installed tools. Short-circuits if no changes needed.

## Step 1: Check if Work is Required

Read README.md and extract:
1. **Brew tools**: All tool names from the `brew install` command (both regular and `--cask`)
2. **Documented tools**: All tool names from the rationale section links

Compare these lists:
- If all brew tools are already documented AND brew command is already sorted (regular alphabetically, then cask alphabetically), report "No changes needed" and **exit early**
- Otherwise, continue to Step 2

## Step 2: Parse and Sort Brew Command

Extract all tool names from the brew command, separating into:
- **Regular tools**: packages without `--cask` prefix
- **Cask tools**: packages with `--cask` prefix

Sort each list alphabetically.

## Step 3: Reformat Brew Command

Reformat the brew command:
- Single logical command using `\` for line continuation
- Wrap at 80 columns maximum
- 4-space indentation on continuation lines
- Regular tools first (sorted), then cask tools (sorted)
- Each cask tool prefixed with `--cask`

Example:
```bash
brew install atuin bat btop carapace direnv espanso eza fzf gdu ghostty \
    git jq lazydocker lazygit neovim starship stow uv yazi yq zoxide \
    --cask claude-code --cask karabiner-elements
```

## Step 4: Generate Documentation for New Tools

For tools not yet documented, use web search to find:
- GitHub repository URL (preferred) or official website
- Brief description of what the tool does

Format each entry as:
```
1. [tool-name](url) - description
```

Rules:
- No bold on links
- No leading articles ("a", "an")
- No capitalization of first word (unless proper noun)
- No ending punctuation
- Keep descriptions short and concise
- Keep numbered list in alphabetical order by tool name
- Delete any placeholder entries (e.g., "1. tbd")
- **Line wrapping**: Maximum 80 columns per line. Wrap at word boundaries
    (never split words). Use 4-space indentation for continuation lines.
    Prefer breaking after punctuation or natural phrase boundaries when possible

Example of wrapped entry:
```
1. [tool-name](https://github.com/org/tool) - description that needs to
    wrap to the next line with 4-space indentation
10. [another-tool](https://github.com/org/another) - longer description
    that wraps correctly for double-digit items too
```

## Step 5: Update README.md

1. Replace the existing brew command with the sorted/formatted version
2. Merge new tool docs into existing rationale list, maintaining alphabetical order

## Output

Report:
- "No changes needed" if short-circuited
- Otherwise: number of new tools documented, any tools where documentation could not be found
