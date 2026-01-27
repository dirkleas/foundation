# Plan: Add CLI/TUI Philosophy Rationale Section

## Goal
Add a new "why cli/tui?" section above "setup" in README.md that articulates the philosophical case for CLI/TUI tools as a complement to unavoidable GUIs.

## Changes

### 1. Add new section after intro, before setup

```markdown
## why cli/tui?

graphical interfaces seem simpler at first glance -- point, click, done. but
that simplicity is a tradeoff:

- **surface consistency, deep chaos**: every app invents its own UX patterns.
  multiply by device, OS, and platform variations. what you learned in one
  context rarely transfers cleanly.
- **hidden state**: where did that setting go? what's actually selected? GUIs
  obscure the state of your system behind layers of menus and modals.
- **geometry struggles**: resolution, scaling, window layouts -- an endless
  negotiation between what you want and what the app allows.
- **automation gap**: scripting GUIs is fragile at best. even state-of-the-art
  AI models struggle to reliably orchestrate graphical interfaces.

cli/tui tools take a different path:

- **explicit**: commands say exactly what they do. no hunting through menus.
- **repeatable**: same input, same output. every time.
- **composable**: small tools that do one thing well, piped together.
- **automatable**: scripts, aliases, hooks -- your workflow becomes code.
- **version-controllable**: text configs live in git. diff, blame, revert.
- **ai-native**: LLMs reason about text naturally. your tools become
  orchestratable.

this isn't about abandoning GUIs entirely. browsers, media editors, visual
design tools -- some work genuinely requires graphical feedback. foundation
provides the cli/tui layer for everything else: the daily operations where
clarity, repeatability, and automation matter most.
```

### 2. Rename "rationale" to "tools"

Change line 55 from `## rationale` to `## tools`

## File to Modify
- `README.md`

## Verification
- Review rendered markdown in GitHub or local preview
- Ensure new section flows logically before setup instructions
