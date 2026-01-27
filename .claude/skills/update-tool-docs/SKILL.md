---
name: update-tool-docs
description: Update README.md tools section with documentation for brew and uv managed tools
---

Update the README.md tools section to document tools from Brewfile (brew managed) and uv tool list (uv managed). Short-circuits if no changes needed.

## Step 1: Check if Work is Required

Read/gather data from:
1. **Brewfile**: Extract all tool names from `brew "toolname"` and `cask "toolname"` lines
2. **uv tool list**: Run `uv tool list` to get installed uv tools (format: `toolname vX.Y.Z`)
3. **README.md tools section**: Extract tool names from both numbered lists (homebrew managed and uv managed)

Compare these lists:
- If all Brewfile tools are documented AND Brewfile is sorted AND all uv tools are documented AND uv tools section is sorted, report "No changes needed" and **exit early**
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

For tools not yet documented in README.md (either brew or uv section), use web search to find:
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
2. Merge new brew/cask tool docs into "homebrew managed tools:" section, maintaining alphabetical order
3. Merge new uv tool docs into "uv managed tools:" section, maintaining alphabetical order

Both sections in README.md follow the same format under "## tools":
```markdown
## tools

here's a summary of the core cli/tui/gui foundation tools:

homebrew managed tools:

1. [tool-name](url) - description
...

uv managed tools:

1. [tool-name](url) - description
...
```

## Output

Report:
- "No changes needed" if short-circuited
- Otherwise: number of new tools documented (brew and uv separately), any tools where documentation could not be found
