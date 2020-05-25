"""Test output of experiments for features under development."""

import pytest
from git.repo.base import Repo

from enguard.experiments import (list_files_since_last_push, list_staged_files,
                                 parse_diff_line,)
from enguard.util import repo_path
from tests.drivers import GitChange, GitDriver
from tests.util import stage_tmp_file


@pytest.mark.experiments
def test_list_staged_files(repo: Repo):
    """Test list_staged_files returns only staged files."""
    driver = GitDriver.from_repo(repo)
    file = driver.stage()
    assert file.where_change_type(GitChange.Add) in list_staged_files(repo)


@pytest.mark.experiments
def test_list_staged_files_is_empty(repo: Repo):
    """Test list_staged_Files returns empty list if nothing staged."""
    assert not list_staged_files(repo)


@pytest.mark.experiments
def test_git_file(repo: Repo):
    pass


@pytest.mark.experiments
def test_list_files_changed_since_last_push():
    driver = GitDriver.pushable_clone()

    temp1 = driver.add("This is a test commit")
    driver.push()

    temp2 = driver.add("This is a test commit 2")
    temp3 = driver.add("This is a test commit 3")

    driver.modify(temp1)
    driver.modify(temp2)
    temp4 = driver.add("This is a test commit 4")

    diff = list_files_since_last_push(driver.repo)
    print(diff[0])
    assert temp1.where_change_type(GitChange.Mod) in diff
    assert temp2.where_change_type(GitChange.Add) in diff
    assert temp3.where_change_type(GitChange.Add) in diff
    assert temp4.where_change_type(GitChange.Add) in diff

    assert driver.is_pristine


@pytest.mark.experiments
def test_list_files_changed_since_last_push_branch_from_master():
    driver = GitDriver.pushable_clone()

    temp1 = driver.add("This is a test commit")
    driver.push()

    driver.branch()

    temp2 = driver.add("This is a test commit 2")
    temp3 = driver.add("This is a test commit 3")

    driver.modify(temp1)
    driver.modify(temp2)
    temp4 = driver.add("This is a test commit 4")

    diff = list_files_since_last_push(driver.repo)
    assert temp1.where_change_type(GitChange.Mod) in diff
    assert temp2.where_change_type(GitChange.Add) in diff
    assert temp3.where_change_type(GitChange.Add) in diff
    assert temp4.where_change_type(GitChange.Add) in diff

    assert driver.is_pristine


@pytest.mark.experiments
def test_list_files_changed_since_last_push_without_origin(repo):
    driver = GitDriver.from_repo(repo)

    temp1 = driver.add("This is a test commit 1")

    driver.branch()

    temp2 = driver.add("This is a test commit 2")
    temp3 = driver.add("This is a test commit 3")

    driver.modify(temp1)
    driver.modify(temp2)
    temp4 = driver.add("This is a test commit 4")

    diff = list_files_since_last_push(driver.repo)
    assert temp1.where_change_type(GitChange.Mod) in diff
    assert temp2.where_change_type(GitChange.Add) in diff
    assert temp3.where_change_type(GitChange.Add) in diff
    assert temp4.where_change_type(GitChange.Add) in diff

    assert driver.is_pristine


@pytest.mark.experiments
def test_parse_diff_line():
    assert parse_diff_line("A\tfilename.txt") == (GitChange("A"), "filename.txt")
    assert parse_diff_line("M\tfile-slug.txt") == (GitChange("M"), "file-slug.txt")


@pytest.mark.experiments
def test_list_files_inbound_from_merge(repo: Repo):
    # TODO: How do we simulate a merge?
    driver = GitDriver.from_repo(repo)

    temp1 = driver.add("This is a test commit 1")

    driver.branch()

    temp2 = driver.add("This is a test commit 2")
    temp3 = driver.add("This is a test commit 3")

    driver.modify(temp1)
    driver.modify(temp2)
    temp4 = driver.add("This is a test commit 4")

    assert driver.is_pristine
