"""Main module."""

import os

import yaml
from enguard.util import get_absolute_repo_path
from pydriller import GitRepository

CONFIG_FILENAME = '.enguard.yml'

DEFAULT_CONF = {
    'hooks': {
        'pre-commit': [
            'echo "Add your pre-commit steps here."',
            'echo "Affected files {{ files.affected }}"'
        ],
        'pre-push': [
            'echo "Add your pre-push steps here."',
            'echo "Affected files {{ files.affected }}"'
        ],
        'post-merge': [
            'echo "Add your post-merge steps here."',
            'echo "Affected files {{ files.affected }}"'
        ],
    }
}


def init(path=None):
    """Initialize enguard in a git repository."""
    if path is None:
        path = os.curdir

    repo = GitRepository(path)

    with open(get_absolute_repo_path(repo, CONFIG_FILENAME), 'w+') as f:
        yaml.safe_dump(DEFAULT_CONF, f)
