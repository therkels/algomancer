import click
import os
from pathlib import Path
from utils.config import load_config


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Algomancer CLI."""
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config()


@cli.command()
def hello() -> None:
    """Prints hello world."""
    click.echo(f"path: {Path.home()}")

@cli.command()
@click.pass_context
def init(ctx: click.Context) -> None:
    """Init the forked code to store problem and testing files."""
    try:
        os.makedirs(ctx.obj["config"]["solved_dir_name"], exist_ok=True)
        os.makedirs(ctx.obj["config"]["attempting_dir_name"], exist_ok=True)
        os.makedirs(ctx.obj["config"]["data_structures_dir_name"], exist_ok=True)
        click.echo("Directories created successfully!")
    except Exception as e:
        click.echo(f"Error creating directories: {e}")

@cli.command()
@click.pass_context
@click.argument("problem", type=str, required=True)
@click.option("-e", "difficulty", flag_value="easy", help="Set difficulty to easy")
@click.option("-m", "difficulty", flag_value="medium", help="Set difficulty to medium")
@click.option("-h", "difficulty", flag_value="hard", help="Set difficulty to hard")
def add_problem(ctx: click.Context, problem: str, difficulty: str) -> None:
    """Add a problem to the attempting folder."""
    if difficulty is None:
        click.echo("Error: You must specify a difficulty using -e, -m, or -h.")
        return
    try:
        if not os.path.exists(os.path.join(ctx.obj["config"]["attempting_dir_name"], difficulty)):
            os.mkdir(os.path.join(ctx.obj["config"]["attempting_dir_name"], difficulty))
        problem_file = os.path.join(ctx.obj["config"]["attempting_dir_name"], difficulty, f"{problem}.py")
        if os.path.exists(problem_file):
            click.echo(f"Problem {problem} already exists.")
            return
        with open(problem_file, "w") as file:
            file.write(f"# Problem: {problem}\n")
            file.write(f"# Difficulty: {difficulty}\n")
            file.write("\n")
            file.write("def solve() -> None:\n")
            file.write("    pass\n")
        click.echo(f"Problem {problem} added successfully!")
    except Exception as e:
        click.echo(f"Error adding problem: {e}")