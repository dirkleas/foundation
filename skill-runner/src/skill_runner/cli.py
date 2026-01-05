"""CLI for running skills."""

import sys
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .core import SkillRunner
from .schema import list_skills, load_skill

app = typer.Typer(
    name="skill",
    help="Run Claude skills from the command line.",
    no_args_is_help=True,
)
console = Console()
err_console = Console(stderr=True)


@app.command()
def run(
    skill_name: Annotated[str, typer.Argument(help="Name of the skill to run")],
    inputs: Annotated[
        list[str] | None,
        typer.Option(
            "--input", "-i",
            help="Input values as name=value pairs (can be repeated)",
        ),
    ] = None,
    model: Annotated[
        str,
        typer.Option("--model", "-m", help="Model to use"),
    ] = "claude-sonnet-4-20250514",
    raw: Annotated[
        bool,
        typer.Option("--raw", "-r", help="Output raw text without formatting"),
    ] = True,
) -> None:
    """Run a skill with optional inputs.

    Inputs can be provided via --input flags or piped via stdin.
    If not provided, inputs with commands will be auto-gathered.
    Uses Claude Code SDK with subscription auth (no API key needed).

    Examples:
        skill run commit-messager
        skill run commit-messager --input diff="$(git diff)"
        git diff | skill run commit-messager
    """
    # Parse input key=value pairs
    input_dict: dict[str, str] = {}
    if inputs:
        for inp in inputs:
            if "=" in inp:
                key, value = inp.split("=", 1)
                input_dict[key] = value
            else:
                err_console.print(f"[red]Invalid input format: {inp}[/red]")
                err_console.print("Use: --input name=value")
                raise typer.Exit(1)

    # Check for stdin
    stdin_content: str | None = None
    if not sys.stdin.isatty():
        stdin_content = sys.stdin.read()

    try:
        runner = SkillRunner(model=model)
        result = runner.run(skill_name, inputs=input_dict, stdin=stdin_content)

        if raw:
            console.print(result, highlight=False, soft_wrap=True)
        else:
            console.print(Panel(result, title=f"[bold]{skill_name}[/bold]"))

    except FileNotFoundError as e:
        err_console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)
    except ValueError as e:
        err_console.print(f"[red]Input error: {e}[/red]")
        raise typer.Exit(1)
    except Exception as e:
        err_console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command(name="list")
def list_cmd(
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Show detailed skill info"),
    ] = False,
) -> None:
    """List available skills."""
    skills = list_skills()

    if not skills:
        console.print("[yellow]No skills found.[/yellow]")
        console.print("\nSkills are loaded from:")
        console.print("  ./.claude/skills/<name>/SKILL.md  (project)")
        console.print("  ~/.claude/skills/<name>/SKILL.md  (global)")
        return

    table = Table(title="Available Skills")
    table.add_column("Name", style="cyan")
    table.add_column("Description")
    if verbose:
        table.add_column("Inputs", style="dim")
        table.add_column("Path", style="dim")

    for skill in skills:
        if verbose:
            table.add_row(
                skill["name"],
                skill["description"],
                ", ".join(skill["inputs"]) or "-",
                skill["path"],
            )
        else:
            table.add_row(skill["name"], skill["description"])

    console.print(table)


@app.command()
def show(
    skill_name: Annotated[str, typer.Argument(help="Name of the skill to show")],
) -> None:
    """Show details about a skill."""
    try:
        skill = load_skill(skill_name)
    except FileNotFoundError as e:
        err_console.print(f"[red]{e}[/red]")
        raise typer.Exit(1)

    console.print(Panel(f"[bold]{skill.name}[/bold]\n{skill.description}"))

    if skill.inputs:
        table = Table(title="Inputs")
        table.add_column("Name", style="cyan")
        table.add_column("Required")
        table.add_column("Auto-gather Command", style="dim")
        table.add_column("Description")

        for name, inp in skill.inputs.items():
            table.add_row(
                name,
                "yes" if inp.required else "no",
                inp.command or "-",
                inp.description,
            )

        console.print(table)

    console.print(f"\n[bold]Output format:[/bold] {skill.output.format}")
    console.print(f"\n[bold]Prompt:[/bold]\n{skill.prompt[:500]}{'...' if len(skill.prompt) > 500 else ''}")


def main() -> None:
    """Entry point."""
    app()


if __name__ == "__main__":
    main()
