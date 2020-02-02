#!/usr/bin/env python

"""Tests for `enguard` package."""

from click.testing import CliRunner

from enguard import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'enguard.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_init_creates_a_default_config_file():
    """Test init command creates the default config file."""
    pass


def test_init_installs_git_hooks():
    """Test init command installs a script for all git hooks."""
    pass
