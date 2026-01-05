"""MCP Server for skill execution."""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

from .core import SkillRunner
from .schema import list_skills, load_skill

server = Server("skill-runner")
runner = SkillRunner()


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    tools = [
        Tool(
            name="run_skill",
            description="Run a Claude skill by name with optional inputs",
            inputSchema={
                "type": "object",
                "properties": {
                    "skill_name": {
                        "type": "string",
                        "description": "Name of the skill to run",
                    },
                    "inputs": {
                        "type": "object",
                        "description": "Input values as key-value pairs (optional - will auto-gather if not provided)",
                        "additionalProperties": {"type": "string"},
                    },
                },
                "required": ["skill_name"],
            },
        ),
        Tool(
            name="list_skills",
            description="List all available skills",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="show_skill",
            description="Show details about a specific skill",
            inputSchema={
                "type": "object",
                "properties": {
                    "skill_name": {
                        "type": "string",
                        "description": "Name of the skill to show",
                    },
                },
                "required": ["skill_name"],
            },
        ),
    ]
    return tools


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name == "run_skill":
        skill_name = arguments["skill_name"]
        inputs = arguments.get("inputs", {})

        try:
            result = runner.run(skill_name, inputs=inputs)
            return [TextContent(type="text", text=result)]
        except FileNotFoundError as e:
            return [TextContent(type="text", text=f"Error: {e}")]
        except ValueError as e:
            return [TextContent(type="text", text=f"Input error: {e}")]
        except Exception as e:
            return [TextContent(type="text", text=f"Error: {e}")]

    elif name == "list_skills":
        skills = list_skills()
        if not skills:
            return [TextContent(type="text", text="No skills found.")]

        lines = ["Available skills:", ""]
        for skill in skills:
            inputs_str = f" (inputs: {', '.join(skill['inputs'])})" if skill["inputs"] else ""
            lines.append(f"- {skill['name']}: {skill['description']}{inputs_str}")

        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "show_skill":
        skill_name = arguments["skill_name"]

        try:
            skill = load_skill(skill_name)
            lines = [
                f"Skill: {skill.name}",
                f"Description: {skill.description}",
                "",
                "Inputs:",
            ]

            for inp_name, inp_def in skill.inputs.items():
                cmd = f" (auto: {inp_def.command})" if inp_def.command else ""
                req = "required" if inp_def.required else "optional"
                lines.append(f"  - {inp_name} [{req}]{cmd}: {inp_def.description}")

            lines.extend([
                "",
                f"Output format: {skill.output.format}",
            ])

            return [TextContent(type="text", text="\n".join(lines))]
        except FileNotFoundError as e:
            return [TextContent(type="text", text=f"Error: {e}")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main() -> None:
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
