#!/usr/bin/env bash

set -eu

flake8 enguard
bandit -r enguard
mypy enguard
