.. |guards| replace:: :term:`guards<guard>`
.. |guard| replace:: :term:`guard`
.. |commit| replace:: :term:`commit`
.. |push| replace:: ::term:`push`

**************
Specifications
**************

Enguard is designed primarily for web developers who:

* |Commit| frequently and often.
* |Push| changes frequently and often.
* Want to avoid commiting and pushing code that breaks builds.
* Want to know if a merge breaks the build.
* See great value in tools like Husky and Precommit but want to
  reduce the feedback loop even further.

I believe that developers can increase their productivity by
doing two things:

#. Increasing the number of feedback loops
#. Shortening the time to feedback in each of those loops

Enguard's goals, as a tool, are to:

* Add a feedback loop between each push to prevent CI (or worse,
  production) from reporting issues local tools can detect.
* Add a feedback loop between each commit to prevent the pre-push
  guard from finding issues that can be detected earlier.
* Allow for instant feedback by watching for file changes and running
  a set of fast checks.
* Shorten the above feedback loops by only analysing code that is
  affected by a change.
* Prevent feedback loops from becoming too long by guarding their
  maximum workload.

Use Cases
=========

#. Developers want to eliminate failing builds and deployments by guarding
   their commits and pushes from common issues.

   #. Provide a bank of configurations for different types of projects.
   #. Detect and suggest appropriate configurations given project
      characteristics.

#. On the flip side, developers want prompt feedback so configured |guards| do
   not get in the way of or slow progress.

   #. Provide a tool-agnostic way to generate appropriate affected files
   #. Provide a configurable max work/time on |guards| to enforce an upper
      limit on feedback cycle time.
   #. Provide tools to monitor and report on the running time of |guards| and
      their constitutient |guards|.

#. Developers want to get up and running quickly to minimise impact on their
   day to day.
#. Developers want to test the tasks defined in their configured |guards| so
   they know each works as intended.
#. Developers want to check their configuration so they know it will work
   before testing their |guards|.
#. Developers want to set up Enguard with an existing configuration because Git
   does not version control hooks.
#. Developers want to limit the scope of a |guard| to a particular set of files
   so |guards| only run against relevant files or not at all.

Terminology
===========

.. glossary::
    Commit
        By **commit**, I mean recording a change to a repository. For example,
        via ``git commit``.

    Push
        By **push**, I mean pushing one or more commits to a remote repository.
        For example, via ``git push``.

    Merge
        By **merge**, I mean any operation that merges recorded changes from
        either branches, for example via ``git merge``, or from remote
        repositories, for example via ``git pull``.

    Guard
        A **guard** is a step or number of steps that must return an exit code
        of 0 to pass, much like a build.
