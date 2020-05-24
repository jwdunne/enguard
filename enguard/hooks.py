from pathlib import Path
from typing import Set

HOOKS_PATH = ".git/hooks"

HOOKS = {
    "applypatch-msg",
    "pre-applypatch",
    "post-applypatch",
    "pre-commit",
    "prepare-commit-msg",
    "commit-msg",
    "post-commit",
    "pre-rebase",
    "post-checkout",
    "post-merge",
    "pre-receive",
    "update",
    "post-receive",
    "post-update",
    "pre-auto-gc",
    "post-rewrite",
    "pre-push",
}

HOOK_SCRIPT = """
#!/usr/bin/env bash

# enguard start
echo "Running enguard"
# enguard end
"""


def hooks_path(base: Path) -> Path:
    return base / HOOKS_PATH


def hooks_exist(existing_hooks: Set[str]) -> bool:
    return HOOKS.issubset(existing_hooks)


def missing_hooks(existing_hooks: Set[str]) -> Set[str]:
    return HOOKS - existing_hooks
