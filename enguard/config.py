"""
Configuration module.

Types:

data Config = Config {
    hooks :: [Hook],
    watchers :: [Watcher],
    hooks :: [Hook]
}

data Hook = Hook GitHook
"""

from pathlib import Path

CONF_PATH = ".enguard.yml"

DEFAULT_CONF = {
    "hooks": {
        "pre-commit": [
            'echo "Add your pre-commit steps here."',
            'echo "Affected files {{ files.affected }}"',
        ],
        "pre-push": [
            'echo "Add your pre-push steps here."',
            'echo "Affected files {{ files.affected }}"',
        ],
        "post-merge": [
            'echo "Add your post-merge steps here."',
            'echo "Affected files {{ files.affected }}"',
        ],
    }
}


def config_path(base: Path) -> Path:
    return base / CONF_PATH
