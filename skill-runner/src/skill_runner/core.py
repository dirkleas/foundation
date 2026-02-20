"""Core skill execution logic."""

import asyncio
import logging
import subprocess
from pathlib import Path

from claude_agent_sdk import ClaudeAgentOptions, query

from .schema import Skill, load_skill

logger = logging.getLogger(__name__)


def _patch_sdk_message_parser() -> None:
    """Patch SDK to gracefully handle unknown message types (e.g. rate_limit_event).

    The claude-agent-sdk raises MessageParseError on unrecognized message types,
    which kills the async generator mid-stream. This wraps parse_message to return
    a SystemMessage for unknown types instead. Safe to call multiple times.
    """
    import claude_agent_sdk._internal.message_parser as mp
    import claude_agent_sdk._internal.client as internal_client
    from claude_agent_sdk.types import SystemMessage

    if getattr(mp.parse_message, "_patched", False):
        return

    _original = mp.parse_message

    def _safe_parse_message(data):
        try:
            return _original(data)
        except Exception:
            msg_type = data.get("type", "unknown") if isinstance(data, dict) else "unknown"
            logger.debug("SDK: unrecognized message type '%s', wrapping as SystemMessage", msg_type)
            return SystemMessage(subtype=msg_type, data=data if isinstance(data, dict) else {})

    _safe_parse_message._patched = True  # type: ignore[attr-defined]
    mp.parse_message = _safe_parse_message
    internal_client.parse_message = _safe_parse_message


_patch_sdk_message_parser()


class SkillRunner:
    """Executes skills via Claude Agent SDK (uses subscription auth)."""

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
        """Run a query via Claude Agent SDK."""
        options = ClaudeAgentOptions(
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
        """Run a skill by name using Claude Agent SDK.

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
