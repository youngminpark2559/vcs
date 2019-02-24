002_git_add

# ======================================================================
# To create f1.txt file
vim f1.txt

# To see contents of f1.txt file
cat f1.txt

# ======================================================================
Run
git status

You wil see:
untracked file
which means you're being in the directory
which is version-managed by git
But git is not tracking the history of the version

# To add f1.txt file to the list 
# in which git tracks version history
git add f1.txt