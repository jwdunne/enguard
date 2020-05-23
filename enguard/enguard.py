"""Main module."""

import os

import yaml
from enguard import config
from enguard.util import repo_path
from pydriller import GitRepository


def init(path=os.curdir):
    """Initialize enguard in a git repository."""
    repo = GitRepository(path)

    with open(repo_path(repo) / config.CONF_PATH, "w+") as f:
        yaml.safe_dump(config.DEFAULT_CONF, f)
