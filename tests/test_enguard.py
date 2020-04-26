#!/usr/bin/env python

"""Tests for `enguard` package."""

import os

import pytest
import yaml
from click.testing import CliRunner
from enguard import cli
from enguard.enguard import DEFAULT_CONF
from enguard.util import get_absolute_repo_path
from pydriller import GitRepository


@pytest.mark.slow
def test_init_creates_a_default_config_file(repo: GitRepository):
    """Test init command creates the default config file."""
    os.chdir(repo.path)

    runner = CliRunner()
    result = runner.invoke(cli.init)

    assert result.exit_code == 0
    assert "Created default config file" in result.output

    with open(get_absolute_repo_path(repo, ".enguard.yml")) as f:
        config = yaml.safe_load(f)
        assert config == DEFAULT_CONF


@pytest.mark.slow
def test_init_installs_git_hooks():
    """Test init command installs a script for all git hooks."""
    pass


@pytest.mark.slow
def test_init_takes_a_path_positional_arg():
    """Test init uses the positional arg as the path to the repo."""
    pass
