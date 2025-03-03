import click
import os


@click.group()
def cli() -> None:
    """Algomancer CLI."""
    pass


@cli.command()
def hello() -> None:
    """Prints hello world."""
    click.echo("hello world!")


@cli.command()
@click.option('--dir', default='new_directory', help='Directory to create')
def init(dir: str) -> None:
    """Create a new directory."""
    try:
        os.makedirs(dir, exist_ok=True)
        click.echo(f"Directory '{dir}' created successfully!")
    except Exception as e:
        click.echo(f"Error creating directory '{dir}': {e}")
