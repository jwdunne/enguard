"""Main module."""

import os

from pydriller import GitRepository

from enguard.io import FileIO
from enguard.config import init_config
from enguard.hooks import install_hooks


def init(path=os.curdir):
    """Initialize enguard in a git repository."""
    repo = GitRepository(path)

    io = FileIO()
    init_config(repo.path, io)
    install_hooks(repo.path, io)
