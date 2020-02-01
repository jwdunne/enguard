# Enguard

Enguard! Your build fails CI. You make a change. Push. You wait for CI,
taking at minimum two minutes, ignoring queues. Then you think "Why not run
fast build steps *before* each commit and each push? And *after* each merge?"

Husky, a great project, saves the day. You prevent code that fails the fastest,
most basic checks using Git hooks. But then your project grows. Now running the
checks on your whole project adds minutes to your feedback loop. The solution?
Run only on files listed in the diff. But which diff? And what about tools that
*don't* support that?

Enter Enguard. Enguard installs git hooks and passes a list of changed files to
each command.


