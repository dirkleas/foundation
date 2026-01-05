"""Skill schema definitions."""

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class SkillInput(BaseModel):
    """Definition of a skill input."""

    command: str | None = Field(
        default=None, description="Shell command to auto-gather this input"
    )
    description: str = Field(default="", description="Human-readable description")
    required: bool = Field(default=True, description="Whether this input is required")


class SkillOutput(BaseModel):
    """Definition of skill output format."""

    format: str = Field(default="text", description="Output format: text, json, markdown")


class Skill(BaseModel):
    """A skill definition."""

    name: str = Field(description="Skill name/identifier")
    description: str = Field(default="", description="What this skill does")
    inputs: dict[str, SkillInput] = Field(
        default_factory=dict, description="Input definitions"
    )
    output: SkillOutput = Field(
        default_factory=SkillOutput, description="Output format"
    )
    prompt: str = Field(description="The prompt template with {{input}} placeholders")

    def render_prompt(self, inputs: dict[str, str]) -> str:
        """Render the prompt template with provided inputs."""
        result = self.prompt
        for key, value in inputs.items():
            result = result.replace(f"{{{{{key}}}}}", value)
        return result


def parse_skill(content: str, name: str = "unknown") -> Skill:
    """Parse a skill from markdown with YAML frontmatter.

    Format:
    ---
    name: skill-name
    description: What it does
    inputs:
      input_name:
        command: shell command to gather
        description: what this input is
    output:
      format: text
    ---

    The prompt content goes here with {{input_name}} placeholders.
    """
    # Split frontmatter and body
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            body = parts[2].strip()
        else:
            frontmatter = ""
            body = content
    else:
        frontmatter = ""
        body = content

    # Parse frontmatter
    if frontmatter:
        meta = yaml.safe_load(frontmatter) or {}
    else:
        meta = {}

    # Convert inputs to SkillInput objects
    raw_inputs = meta.get("inputs", {})
    inputs = {}
    for inp_name, inp_def in raw_inputs.items():
        if isinstance(inp_def, dict):
            inputs[inp_name] = SkillInput(**inp_def)
        else:
            inputs[inp_name] = SkillInput(description=str(inp_def))

    # Convert output
    raw_output = meta.get("output", {})
    if isinstance(raw_output, dict):
        output = SkillOutput(**raw_output)
    else:
        output = SkillOutput(format=str(raw_output) if raw_output else "text")

    return Skill(
        name=meta.get("name", name),
        description=meta.get("description", ""),
        inputs=inputs,
        output=output,
        prompt=body,
    )


def load_skill(name: str, search_paths: list[Path] | None = None) -> Skill:
    """Load a skill by name from known paths.

    Search order:
    1. ./.claude/skills/<name>/SKILL.md (project)
    2. ~/.claude/skills/<name>/SKILL.md (user global)
    3. Custom search paths
    """
    if search_paths is None:
        search_paths = []

    paths_to_check = [
        Path.cwd() / ".claude" / "skills" / name / "SKILL.md",
        Path.home() / ".claude" / "skills" / name / "SKILL.md",
        *[p / name / "SKILL.md" for p in search_paths],
        *[p / f"{name}.md" for p in search_paths],
    ]

    for path in paths_to_check:
        if path.exists():
            content = path.read_text()
            return parse_skill(content, name)

    searched = "\n  ".join(str(p) for p in paths_to_check)
    raise FileNotFoundError(f"Skill '{name}' not found. Searched:\n  {searched}")


def list_skills(search_paths: list[Path] | None = None) -> list[dict[str, Any]]:
    """List all available skills."""
    if search_paths is None:
        search_paths = []

    all_paths = [
        Path.cwd() / ".claude" / "skills",
        Path.home() / ".claude" / "skills",
        *search_paths,
    ]

    skills = []
    seen = set()

    for base_path in all_paths:
        if not base_path.exists():
            continue
        for skill_dir in base_path.iterdir():
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
                if skill_file.exists() and skill_dir.name not in seen:
                    seen.add(skill_dir.name)
                    try:
                        skill = parse_skill(skill_file.read_text(), skill_dir.name)
                        skills.append({
                            "name": skill.name,
                            "description": skill.description,
                            "path": str(skill_file),
                            "inputs": list(skill.inputs.keys()),
                        })
                    except Exception:
                        pass  # Skip malformed skills

    return skills
