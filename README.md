# Enguard <!-- omit in toc -->

Build tight feedback loops. In minutes.

TODO: Insert 5 minute setup gif

## Table of Contents <!-- omit in toc -->

- [Getting Started](#getting-started)
- [Usage](#usage)
  - [Initialise](#initialise)
  - [Configuration](#configuration)
  - [Simulating hooks](#simulating-hooks)
  - [Running guards](#running-guards)
  - [Watching for changes](#watching-for-changes)
    - [Notes on Watching](#notes-on-watching)
- [Why Enguard](#why-enguard)
  - [The Solution](#the-solution)
  - [Real-time Feedback](#real-time-feedback)
  - [Stopping Common Build Failures](#stopping-common-build-failures)

## Getting Started

To install:

```bash
pip install enguard
enguard init
```

## Usage

```text
Usage: enguard [command] [flags]

Displays help info.

Options:

    -f, --enguard-file=FILE    Use enguard file (default: .enguard.yml)
    --verbose                  Provide more feedback
    -v, --version              Output Enguard's version

Commands:

    - init
    - run
    - watch
```

### Initialise

```text
Usage: enguard init [options]

Initialises enguard hooks and enguard config file.
```

Example:

```bash
enguard init
```

`enguard init` creates a new config file, if one doesn't exist, and initialise
git hooks for a project. This command should be run in each local development
environment.

> _Tip:_ Use one command to initialise your project for new developers. This is
> the natural home for `enguard init`

### Configuration

Configure your project using Enguard's `.enguard.yml` config file:

```yaml
hooks:
  pre-commit:
    - lint-*
    - rapid-test*
  pre-push:
    - lint-*
    - fast-test*

watch:
  - lint-*
  - rapid-test*

guards:
  lint-python:
    glob: "**/*.py",
    run:
      - 'echo {{ info.diff }} | flake8 --diff'
      - 'bandit -r {{ info.affected }}'
      - 'mypy --incremental'
      - >
          xenon
            --max-absolute 'B'
            --max-modules 'A'
            --max-average 'A'

  lint-docs:
    glob: '**/*.md'
    run: 'yarn markdownlint {{ info.affected }}'

  lint-config:
    glob: '**/*.yml'
    run: 'yamllint {{ info.affected }}'

  rapid-test-python:
    glob: "**/*.py"
    stategy: 'coverage'
    run: >
        pytest
            --cov-config='setup.cfg'
            --cov='enguard'
            -m 'not slow'

  fast-test-python:
    glob: "**/*.py"
    stategy: 'coverage'
    run: >
        pytest
            --cov-config='setup.cfg'
            --cov='enguard'
            -m 'rapid, slow'
```

### Simulating hooks

```text
Usage: enguard run-hook hook_name
```

Example:

```bash
$ enguard run-hook pre-commit
$ echo "Failed? $?"
0
```

Running `enguard run-hook` with a hook name simulates the actions you have
configured for the hook. This is the same command that git calls when running
hooks.

### Running guards

```text
Usage: enguard run-guard guard_name

Options:

    --glob=GLOB          A glob of files this guard operates on
    --strategy=STRATEGY  Determine affected files using STRATEGY
```

Example:

```bash
$ enguard run-guard fast-test-python
$ echo "Failed? $?"
0
```

Running `enguard run-guard` with a guard name runs an individual guard. Options
are available to override config values.

### Watching for changes

Usage:

```text
Usage: enguard watch
```

Example:

```bash
$ enguard watch
TODO: Work out interface for watch mode
```

#### Notes on Watching

As a developer, I'd want feedback at-the-point of use. This implies editor
integration, e.g with VS Code. So we must provide a way to query collected
statistics.

I'm going to leave this off the initial release.

## Why Enguard

Your build fails in CI. A linting issue. You forgot to lint before pushing. To
tell you that, your CI server:

1. Initialises the environment
2. Checks out your project
3. Installs (or loads cached) dependencies
4. Analyses all files
5. Runs all tests, from fastest to slowest
6. Builds your project
7. Deploys

This takes time and costs your company money in server usage. And the feedback
takes minutes, disrupting your flow.

### The Solution

To solve this problem, you need to catch common failures **fast**. Instant
feedback is best. In real-time, before each commit, before each push and after
every merge.

But linting all files and running all tests is still slow - limiting feedback
throughput. And, worse, harming your flow.

### Real-time Feedback

With Enguard, you can refine this feedback loop further. With a watcher, you can
get feedback on affected files in real time.

### Stopping Common Build Failures

To stop common build failures, Enguard guards against commiting and pushing
files that will break the build. But not on every file. Enguard limits the
fileset to affected files only.
