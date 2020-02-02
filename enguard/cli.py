"""Console script for enguard."""
import sys

import click
import enguard


@click.group()
def main(args=None):
    pass


@click.command()
def init(args=None):
    """Initialize a project with enguard."""
    enguard.enguard.init()
    click.echo("Created default config file")


main.add_command(init)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
