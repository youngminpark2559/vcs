003_create_version_with_commit

# ======================================================================
# To specify the member who writes versions, run
git config --global user.name Name
git config --global user.email Email

If you commit, the project has new version
which contains information of author.

# ======================================================================
# Run with writing commit message
git commit

which means new version is created

# ======================================================================
# To see various infomation about commit
git log

# ======================================================================
You edit source file and run
git status

You will see the message like
modified

You can't proceed "commit" in this status

You first should add f1.txt file into the list 
for which git tracks version by running
git add f1.txt

When you create a new file,
to let git to track version of this file,
you should first use 
git add

When you create a new version
from the file which is being tracked in version,
you first should use
git add

Then, you can do
git commit
