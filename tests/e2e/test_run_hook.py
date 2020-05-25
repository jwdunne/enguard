"""Tests for `enguard run-hook` command."""

import pytest
from click.testing import CliRunner

from enguard.cli import run_hook
from tests.util import exit_ok


@pytest.mark.acceptance
def test_run_hook_runs_a_hook_by_name():
    runner = CliRunner()
    result = runner.invoke(run_hook, ["pre-commit"])
    assert exit_ok(result.exit_code)
    assert "Running hook: pre-commit" in result.stdout
