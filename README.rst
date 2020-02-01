
Enguard
=======

Enguard! Your build fails CI. You make a change. Push. You wait for CI,
taking at minimum two minutes, ignoring queues. Then you think "Why not run
fast build steps *before* each commit and each push? And *after* each merge?"

Husky, a great project, saves the day. You prevent code that fails the fastest,
most basic checks using Git hooks. But then your project grows. Now running the
checks on your whole project adds minutes to your feedback loop. The solution?
Run only on files listed in the diff. But which diff? And what about tools that
*don't* support that?

Enter Enguard. Get rapid feedback by analysing affected files only. Enguard
installs git hooks and passes a list of changed files to each command, using
sane (but configurable) ranges for each hook.

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

Each hook takes a list of commands to run when triggered. Each command is passed
a list of files affected by the hook action:

.. code-block:: bash

   <insert example hook configuration>

You can configure the default commit ranges and diff parameters too:

.. code-block:: bash

   <insert example commit range config using defaults>
