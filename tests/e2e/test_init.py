#!/usr/bin/env python

"""Tests for `enguard init` command."""

import os

import pytest
import yaml
from click.testing import CliRunner
from pydriller import GitRepository

from enguard.cli import cli
from enguard.config import DEFAULT_CONF, config_path
from enguard.hooks import hooks_path
from enguard.util import repo_path
from tests.util import hooks_ok


@pytest.mark.acceptance
def test_init_configures_env_from_scratch(repo: GitRepository):
    """
    Test init command creates the default config file.
    Context -> a -> Assertion -> TestResult ()
    """

    path = repo_path(repo)

    runner = CliRunner()
    result = runner.invoke(cli, ["--path", path, "init"])
    assert result.exit_code == 0, result.exception

    with open(config_path(path)) as f:
        config = yaml.safe_load(f)
        assert config == DEFAULT_CONF

    with os.scandir(hooks_path(path)) as entries:
        assert hooks_ok(entries)

    # TODO: default config must result in 'noop' for all enguard actions
    # TODO: git actions must invoke enguard
