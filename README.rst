
Enguard
=======

Your build fails in CI. A linting issue. You forgot to lint before pushing. To
tell you that, your CI must:

1. Initialise the environment
2. Check out your project
3. Install (hopefully cached) dependencies
4. Run the linter on all files

A frustrating experience. But what if there's a way to **stop** you from
pushing these errors? A way to never forget?

Enter Enguard. Get rapid feedback by analysing only the affected files on any
git hook. Enguard captures all hooks and passes a list of changed files to each
command, using sane (but configurable) ranges for each hook.

Getting Started
---------------

Install:

.. code-block:: bash

   pip install enguard
   cd ./my-project
   enguard init

You can also specify the working directory:

.. code-block:: bash

    enguard init --dir=./my-project

Enguard catches all git hook triggers and creates a default config file:

.. code-block:: yaml

    ---

    hooks:
        pre-commit:
            - echo "Add your pre-commit steps here."
            - echo "Affected files {{ files.affected }}"
        pre-push:
            - echo "Add your pre-push steps here."
            - echo "Affected files {{ files.affected }}"
        post-merge:
            - echo "Add your post-merge steps here."
            - echo "Affected files {{ files.affected }}"

You can list any number of steps for any git hook you need. Using template
variables, you can give a list of affected files to each command.

You can test the steps for each hook by running, for example:

.. code-block:: bash

  enguard run pre-commit

You can configure the default commit ranges and diff parameters too:

.. code-block:: yaml

    ---

    hooks:
        pre-commit:
            steps:
                - echo "Add your pre-commit steps here."
                - echo "Affected files {{ files.affected }}"
            diff:
                range: HEAD^
                args:
                    staged: False
