---
name: commit-messager
description: Generate conventional commit messages from git diffs
inputs:
  diff:
    command: git diff --cached
    description: Staged git changes to generate commit message for
output:
  format: text
---

OUTPUT RULE: Your response is the commit message. Nothing else. No intro. No fences. No explanation.

START YOUR RESPONSE WITH ONE OF THESE EXACT PREFIXES:
- feat:
- feat(scope):
- fix:
- fix(scope):
- docs:
- docs(scope):
- refactor:
- refactor(scope):
- style:
- perf:
- test:
- build:
- ci:
- chore:
- revert:

If you write anything before the type prefix, you have failed.
If you use backticks anywhere, you have failed.
If you write "Here's" or "Based on", you have failed.

## Format

type(scope): description (max 50 chars, imperative mood, no period)

 - Body line explaining why (optional, wrap at 72 chars)

Refs: #123 (optional footer)

## Examples

feat(model): add timestamp fields for answer duration

 - Replace single timestamp with start/end to capture discussion length.

---

fix(api): handle null response from upstream

---

docs: update README installation steps

---

refactor(utils): extract validation logic to helper

## Diff

{{diff}}
