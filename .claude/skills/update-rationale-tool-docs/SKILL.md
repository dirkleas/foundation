---
name: update-rationale-tool-docs
description: Update README.md rationale section with documentation for brew-installed tools
---

Update the README.md rationale section to document tools from Brewfile. Short-circuits if no changes needed.

## Step 1: Check if Work is Required

Read both files:
1. **Brewfile**: Extract all tool names from `brew "toolname"` and `cask "toolname"` lines
2. **README.md rationale section**: Extract all tool names from the numbered list links

Compare these lists:
- If all Brewfile tools are already documented AND Brewfile is already sorted (brew entries alphabetically, then cask entries alphabetically), report "No changes needed" and **exit early**
- Otherwise, continue to Step 2

## Step 2: Parse and Sort Brewfile

Extract all tool names from Brewfile, separating into:
- **Brew tools**: lines matching `brew "toolname"`
- **Cask tools**: lines matching `cask "toolname"`

Sort each list alphabetically by tool name.

## Step 3: Reformat Brewfile

Rewrite Brewfile with sorted entries:
- Header comment: `# Foundation CLI/TUI tools - sorted alphabetically`
- All `brew "toolname"` entries (sorted alphabetically)
- Blank line
- Header comment: `# Casks - sorted alphabetically`
- All `cask "toolname"` entries (sorted alphabetically)

Example:
```ruby
# Foundation CLI/TUI tools - sorted alphabetically
brew "atuin"
brew "bat"
brew "btop"

# Casks - sorted alphabetically
cask "claude-code"
cask "karabiner-elements"
```

## Step 4: Generate Documentation for New Tools

For tools not yet documented in README.md rationale section, use web search to find:
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

## Step 5: Update Files

1. Write the sorted Brewfile if changes were needed
2. Merge new tool docs into existing README.md rationale list, maintaining alphabetical order

## Output

Report:
- "No changes needed" if short-circuited
- Otherwise: number of new tools documented, any tools where documentation could not be found
