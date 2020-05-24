#!/usr/bin/env python

"""Tests for `enguard` package."""

import pytest
import yaml
from click.testing import CliRunner
from pydriller import GitRepository

from enguard.cli import cli
from enguard.config import DEFAULT_CONF, config_path
from enguard.hooks import hooks_path
from enguard.util import complement, repo_path
from tests.util import dir_context, hooks_ok


def conf_is_ok(conf):
    return conf == DEFAULT_CONF


def exit_is_ok(exit_code):
    return exit_code == 0


def cli_context(path, assertion) -> bool:
    runner = CliRunner()
    result = runner.invoke(cli, ["--path", path, "init"])
    assert assertion(result.exit_code), result.exception


def yaml_context(path, assertion):
    with open(path) as f:
        config = yaml.safe_load(f)
        assert assertion(config)


@pytest.mark.acceptance
def test_init_configures_env_from_scratch(repo: GitRepository):
    """
    Test init command creates the default config file.
    Context -> a -> Assertion -> TestResult ()
    """

    path = repo_path(repo)
    cli_context(path, exit_is_ok)
    yaml_context(config_path(path), conf_is_ok)
    dir_context(hooks_path(path), complement(hooks_ok))

    # TODO: default config must result in 'noop' for all enguard actions
    # TODO: git actions must invoke enguard
