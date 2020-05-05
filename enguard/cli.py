"""Console script for enguard."""
import sys

import click
import enguard


@click.group()
def cli(args=None):
    pass


@cli.command()
def init(args=None):
    """Initialise enguard hooks and config file."""
    enguard.enguard.init()
    click.echo("Created default config file")


@cli.command("run-hook")
@click.argument("hook_name", type=str)
def run_hook(hook_name):
    """Run an enguard hook manually."""
    click.echo(f"Running hook: {hook_name}")


@cli.command("run-guard")
@click.argument("guard_name", type=str)
@click.option("--glob", type=str, default="*")
@click.option("--strategy", type=str, default="files")
def run_guard(guard_name, glob, strategy):
    """Run an enguard guard manually."""
    click.echo(f"Running guard: {guard_name}")
    click.echo(f"Over: {glob}")
    click.echo(f"Using strategy: {strategy}")


@cli.command("watch")
def watch():
    click.echo(f"Watching...")


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
