from pathlib import Path
from functools import partialmethod

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


def hooks_path(base: Path) -> Path:
    return base / HOOKS_PATH


def hooks_exist(existing_hooks: set) -> bool:
    return HOOKS.issubset(existing_hooks)


def missing_hooks(existing_hooks: set) -> bool:
    return HOOKS - existing_hooks
