import os
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


def hook_script(hook_name: str) -> str:
    return f"""
#!/usr/bin/env bash

set -eu

# enguard start
enguard run-hook {hook_name}
# enguard end
"""


def hooks_path(base: Path) -> Path:
    return base / HOOKS_PATH


def hooks_exist(existing_hooks: Set[str]) -> bool:
    return HOOKS.issubset(existing_hooks)


def missing_hooks(existing_hooks: Set[str]) -> Set[str]:
    return HOOKS - existing_hooks


def install_hook(hook_name: str, base: Path):
    path = hooks_path(base) / hook_name
    with open(path, "w") as f:
        f.write(hook_script(hook_name))
        os.chmod(path, 0o600)
