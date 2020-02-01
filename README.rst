
Enguard
=======

Your build fails in CI. A linting issue. You forgot to lint before pushing. To
tell you that, your CI must:

1. Initialise the environment
2. Check out your project
3. Install (hopefully cached) dependencies
4. Run the linter on all files

But what if there's a way to **stop** you from pushing these errors? A way
to never forget?

Enter Enguard. Get rapid feedback by analysing affected files only on any git
hook. Enguard captures all hooks and passes a list of changed files to each
command, using sane (but configurable) ranges for each hook.

Getting Started
---------------

Install:

.. code-block:: bash

   pip install enguard

In your project, run:

.. code-block:: bash

   enguard init

Enguard installs a catch-all git hook and creates a default config file:

.. code-block:: bash

   <insert base config>

Each hook takes a list of commands to run when triggered. Each command is
passed a list of files affected by the hook action:

.. code-block:: yaml

   TOD: insert example hook configuration

You can test the steps for each hook by running, for example:

.. code-block:: bash

  enguard run pre-commit

You can configure the default commit ranges and diff parameters too:

.. code-block:: yaml

   TODO: insert example commit range config using defaults

