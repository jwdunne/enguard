#!/usr/bin/env python

"""Tests for `enguard` package."""

import pytest
import yaml
import os
from typing import List
from functools import partial
from operator import eq, is_not
from click.testing import CliRunner
from enguard.cli import cli
from enguard.hooks import hooks_path, hooks_exist
from enguard.config import DEFAULT_CONF, config_path
from enguard.util import repo_path, compose, complement, prop, identity
from pydriller import GitRepository


default_conf_ok = partial(eq, DEFAULT_CONF)
exit_ok = partial(eq, 0)

repo_config_path = compose(config_path, repo_path)
repo_hooks_path = compose(hooks_path, repo_path)


def cli_context(cmd: List[str], assertion) -> bool:
    runner = CliRunner()
    result = runner.invoke(cli, ["--path", cmd, "init"])
    assert assertion(result.exit_code), result.exception


def yaml_context(path, assertion):
    with open(path) as f:
        config = yaml.safe_load(f)
        assert assertion(config)


def dir_context(path, assertion):
    with os.scandir(path) as entries:
        assert assertion(entries)


@pytest.mark.acceptance
def test_init_configures_env_from_scratch(repo: GitRepository):
    """
    Test init command creates the default config file.
    Context -> a -> Assertion -> TestResult ()
    """

    file_names_set = compose(set, partial(map, prop("name")))
    files_ok = complement(compose(hooks_exist, file_names_set))

    tests = [
        (cli_context, identity, exit_ok),
        (yaml_context, config_path, default_conf_ok),
        (dir_context, hooks_path, files_ok),
    ]

    for (ctx, path, ok) in tests:
        ctx(path(repo_path(repo)), ok)


@pytest.mark.acceptance
def test_init_takes_a_path_positional_arg():
    """Test init uses the positional arg as the path to the repo."""
    assert True
