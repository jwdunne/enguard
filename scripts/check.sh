#!/usr/bin/env bash

set -eu

PYTHON_VERSIONS=(3.8 3.7 3.6)

for version in ${PYTHON_VERSIONS[@]}; do
    make check "PYTHON_VERSION = ${version}"
done
