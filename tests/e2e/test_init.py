#!/usr/bin/env python

"""Tests for `enguard` package."""

import pytest
import yaml
import os
from typing import List
from click.testing import CliRunner
from enguard.cli import cli
from enguard.hooks import hooks_path, hooks_exist
from enguard.config import DEFAULT_CONF, config_path
from enguard.util import repo_path, complement
from pydriller import GitRepository


def conf_is_ok(conf):
    return conf == DEFAULT_CONF


def exit_is_ok(exit_code):
    return exit_code == 0


def entries_to_hook_names(entries):
    return {file.name for file in entries}


def files_ok(entries):
    return hooks_exist(entries_to_hook_names(entries))


def cli_context(path, assertion) -> bool:
    runner = CliRunner()
    result = runner.invoke(cli, ["--path", path, "init"])
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

    path = repo_path(repo)
    cli_context(path, exit_is_ok)
    yaml_context(config_path(path), conf_is_ok)
    dir_context(hooks_path(path), complement(files_ok))
