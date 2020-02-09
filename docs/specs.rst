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
   #. Provide a comprehensive set of resources that complement enguard, e.g:

      #. Segmenting tests by speed for test framework x.
      #. Converting slower tests into faster tests in framework x.
      #. Profiling testing frameworks to highlight which ones slow feedback
         cycles the most.
      #. Profiling linters and linting checks to show which contribute the most
         to slower feedback loops.

#. On the flip side, developers want prompt feedback so configured |guards| do
   not get in the way of or slow progress.

   #. Generate appropriate affected files per each cycle, providing strategies
      based on the type of |guard|. For example:

      #. Linting only requires a list of files changed.
      #. Testing requires a list of tests that exercise code affected by a set
         of changes. The set of tests and code exercised is often wider than
         the actual change itself.

   #. Allow developers to configure filters so that guards only run on certain
      files, or not at all if no files match.
   #. Enforce a configurable max work/time on |guards| to ensure a feedback
      loop's cycle time remains acceptable to the developer.
   #. Monitor and report on the running time of |guards| and their
      constitutient |guards|.
   #. Use heuristics and analyses to prioritise the fastest route to feedback:

      #. Code that frequently fails guards.
      #. Bug hotspots.
      #. Fastest guards.

   #. Support fail-fast so that Enguard stops as soon as it encounters a
      failing guard, providing fast feedback
   #. Support running all guards regardless of failures so that the developer
      can fix all errors at once.
   #. Support naming guards so it's easy for the developer to identify
      failures.

#. Developers want to get up and running quickly to minimise impact on their
   day to day.

   #. Initialise enguard in a single command, creating a default config file
      and git hooks.
   #. Detect use of Husky or Precommit and provide options to either replace,
      integrate or install alongside.
   #. Provide pre-made configurations for common stacks, asking the developer
      which tools to install and use.
   #. Detect common stacks and recommend recipes that make enguard 'just work'
      out of the box.
   #. Allow developers to extend enguard with unforseen stacks and
      configurations to foster an ecosystem.
   #. Support other version control systems to widen applicability.

#. Developers want to test the tasks defined in their configured |guards| so
   they know each works as intended.

   #. Provide commands to invoke a guard outside of the context of a hook.
   #. In fact, use those commands to invoke enguard through hooks so that the
      entry-point is consistent across all actors.
   #. Provide a light testing framework that:

      #. Creates a sandbox clone of their existing repository and enguard
         config.
      #. Allows developers to specify expected results given certain actions.
      #. Reports on passes and failures, providing confidence in guard
         configurations.

#. Developers want to check their configuration so they know it will work
   before testing their |guards|.

     #. Provide a linting tool as part of enguard so that developers can check
        their configuration.
     #. Allow the linting tool to be run as a guard, making enguard check
        itself on, for example, config changes.
     #. Provide working, out-of-the-box configurations for common stacks.

#. Developers want to set up Enguard with an existing configuration because Git
   does not version control hooks.
#. Developers want a smooth exit path so Enguard must uninstall and leave no
   traces behind without affecting other files.

Roadmap
=======

I need this tool on my own projects, including this one. Must-haves are:

#. Initialising on an unconfigured repository
#. Initialising on a configured repository without hooks
#. Running each guard manually
#. Git support only
#. A way to filter affected files so that guards only run on particular files.
#. Fail-fast **and** find all failings.

This should be enough for a initial release, so I can get real user feedback.
But I know I would soon need the following features:

#. Naming guards for easier identification.
#. Strategy for knowing which tests to run for both python, PHP and JS.
#. Migrating from projects that use Husky.
#. A watcher for real-time feedback on certain guards.
#. Priotising for faster feedback.
#. Limit on max guard running time.

To be a good sport, for full, public release, we would need:

#. Migration *from* existing git hook tools.
#. Integration *with* existing git hook tools.
#. Work in tandem *with* existing git hook tools.
#. Smooth uninstallation with no mess left behind.

Use Case 1
**********

Developer sets up enguard on an unconfigured project and enguard protects
against commiting and pushing files containing errors or violations of
standards.

#. Developer initialises enguard on a version-controlled project.

   #. Enguard could not find a git repo in the specified path.

      #. Report error to the developer.
      #. Explain next steps.
      #. Exit with error code.

   #. Enguard finds an existing enguard config file.

      #. Report to developer and continue.

   #. Enguard does not have permission to read or write files in the directory.

      #. Report error to the developer.
      #. Exit with error code.

   #. Enguard finds existing, non-Enguard git hooks.

      #. Report to developer.
      #. Append to hook and continue.

#. Developer changes version-controlled files.
#. Developer attempts to commit changes.
#. Enguard runs configured precommit guards.

   #. Enguard could not read configuration file.
   #. Enguard encounters an invalid configuration file.
   #. Enguard could not run command in specified guard.
   #. Enguard could not find relevant affected files for a guard.
   #. Developer attempts to commit a large number of files.

#. Enguard allows the commit given all guards pass.

   #. Enguard encounters a failing guard.

#. Developer pushes changes to a remote repo.
#. Enguard runs configured prepush guards.

   #. Enguard could not read configuration file.
   #. Enguard encounters an invalid configuration file.
   #. Enguard could not run command in specified guard.
   #. Enguard could not find relevant affected files for a guard.
   #. Developers attempts to push a large number of files.

#. Enguard allows the push given all guards pass.

   #. Enguard encounters a failing guard.

Terminology
===========

.. glossary::
    Commit
        Recording a change to a repository. For example, via ``git commit``.

    Push
        Pushing one or more commits to a remote repository. For example, via ``git push``.

    Merge
        Any operation that merges recorded changes from either branches, for
        example via ``git merge``, or from remote repositories, for example via
        ``git pull``.

    Guard
        A step or number of steps that must return an exit code of 0 to pass, much like a build.
