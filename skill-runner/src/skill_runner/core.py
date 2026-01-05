"""Core skill execution logic."""

import asyncio
import subprocess
from pathlib import Path

from claude_code_sdk import ClaudeCodeOptions, query

from .schema import Skill, load_skill


class SkillRunner:
    """Executes skills via Claude Code SDK (uses subscription auth)."""

    def __init__(
        self,
        model: str = "claude-sonnet-4-20250514",
        max_turns: int = 1,
        search_paths: list[Path] | None = None,
    ):
        self.model = model
        self.max_turns = max_turns
        self.search_paths = search_paths or []

    def gather_input(self, command: str) -> str:
        """Execute a shell command to gather input."""
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 and result.stderr:
            raise RuntimeError(f"Command failed: {command}\n{result.stderr}")
        return result.stdout

    def resolve_inputs(
        self, skill: Skill, provided: dict[str, str]
    ) -> dict[str, str]:
        """Resolve all inputs - use provided values or auto-gather."""
        resolved = {}

        for name, input_def in skill.inputs.items():
            if name in provided:
                resolved[name] = provided[name]
            elif input_def.command:
                resolved[name] = self.gather_input(input_def.command)
            elif input_def.required:
                raise ValueError(
                    f"Missing required input '{name}' and no command to auto-gather"
                )

        return resolved

    async def _query(self, prompt: str) -> str:
        """Run a query via Claude Code SDK."""
        options = ClaudeCodeOptions(
            model=self.model,
            max_turns=self.max_turns,
        )

        result_parts = []
        async for message in query(prompt=prompt, options=options):
            if hasattr(message, "content"):
                result_parts.append(message.content)

        return "".join(result_parts).strip()

    def run(
        self,
        skill_name: str,
        inputs: dict[str, str] | None = None,
        stdin: str | None = None,
    ) -> str:
        """Run a skill by name using Claude Code SDK.

        Args:
            skill_name: Name of the skill to run
            inputs: Dict of input name -> value (optional, will auto-gather if not provided)
            stdin: If provided and skill has a single input, use this as that input

        Returns:
            The skill output as a string
        """
        skill = load_skill(skill_name, self.search_paths)
        provided = inputs or {}

        # Handle stdin for single-input skills
        if stdin and len(skill.inputs) == 1 and not provided:
            input_name = list(skill.inputs.keys())[0]
            provided[input_name] = stdin

        # Resolve all inputs
        resolved = self.resolve_inputs(skill, provided)

        # Render prompt with inputs
        prompt = skill.render_prompt(resolved)

        return asyncio.run(self._query(prompt))

    def run_skill(self, skill: Skill, inputs: dict[str, str]) -> str:
        """Run a pre-loaded skill with resolved inputs."""
        prompt = skill.render_prompt(inputs)
        return asyncio.run(self._query(prompt))
