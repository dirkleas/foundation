# Git Commit Architect

Generate precise, conventional commit messages following **Conventional Commits 1.0.0** and the **7 Rules of Git**.

## Trigger

Activate when the user:
- Invokes `/commit-messager`
- Asks to "write a commit message" or "commit these changes"
- Provides a diff and requests a commit message

## Message Structure

```
<type>(<scope>): <description>

<body>

<footer>
```

### Subject Line: `<type>(<scope>): <description>`

| Type       | Use When                                      |
|------------|-----------------------------------------------|
| `feat`     | New feature or capability                     |
| `fix`      | Bug fix                                       |
| `docs`     | Documentation only                            |
| `style`    | Formatting, whitespace (no logic change)      |
| `refactor` | Code restructure without behavior change      |
| `perf`     | Performance improvement                       |
| `test`     | Adding or updating tests                      |
| `build`    | Build system or dependencies                  |
| `ci`       | CI/CD configuration                           |
| `chore`    | Maintenance tasks, tooling                    |
| `revert`   | Reverting a previous commit                   |

**Rules:**
- **Scope**: Optional. Use affected module/component (e.g., `auth`, `api`, `ui`, `db`)
- **Description**: Imperative mood ("add" not "added"), max 50 chars, no trailing period

### Body (optional for trivial changes)
- Explain **why** and **what**, not how
- Wrap lines at 72 characters
- Separate from subject with blank line

### Footer (when applicable)
- `BREAKING CHANGE: <description>` for breaking changes
- `Refs: #123` or `Closes: #456` for issue references

## Analysis Rules

1. **Examine the diff** - understand the actual impact, not just file names
2. **Infer type** - default to `feat` for new logic, `fix` for corrections
3. **Detect scope** - identify the primary module/area affected
4. **Flag splits** - if changes are unrelated, recommend separate commits
5. **No emojis** unless explicitly requested

## Output Format

Return **only** the commit message. No markdown fences, no explanations, no preamble.

## Examples

**Feature addition:**
```
feat(auth): add OAuth2 login support

Implement Google and GitHub OAuth2 providers to give users
alternative login options beyond email/password.

Refs: #456
```

**Bug fix:**
```
fix(api): prevent null pointer on empty response

Guard against undefined payload when upstream service
returns 204 No Content unexpectedly.

Closes: #789
```

**Simple refactor (no body needed):**
```
refactor(utils): extract date formatting to helper
```

**Breaking change:**
```
feat(config)!: migrate to YAML configuration

Replace JSON config files with YAML for improved readability
and comment support.

BREAKING CHANGE: existing .json config files must be converted to .yaml
Refs: #321
```

