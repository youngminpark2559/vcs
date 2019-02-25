027_mechanism_of_branch

# ======================================================================
# Create gitfth directory
mkdir gitfth

# Initialize gitfth directory
git init

# ======================================================================
After "git init", files are generated in .git directory

In those files, see "HEAD" file

In the contents of "HEAD" file, 
"ref:refs/heads/master" is written.

"refs/heads/master" is a path of a file, 
which doesn't exist yet.

# ======================================================================
touch f1.txt
cat > f1.txt
a
CTRL+D

# ======================================================================
# Upload f1.txt onto the stage
git add f1.txt

# ======================================================================
# Take a snapshot of files
git commit -m "1"

# ======================================================================
Go to gistory (or .git directory) 
and find .git/refs/heads/master

.git/refs/heads/master file has ID value
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:11:30.png

# ======================================================================
Click that link

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:11:59.png

ID value indicates your commit you did just ago

# ======================================================================
Clink .git/HEAD file

click ref:refs/heads/master

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:14:16.png

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:14:54.png

# ======================================================================
# Edit f1.txt by adding b under a
vim f1.txt
a
b

# Commit again
git commit -am "2"

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:16:14.png

Go to gistory
Click refs/heads/master file 

Contents of that file has been changed, indicating "commit 2"

# ======================================================================
Summary

1. When you do "git init" in your working directory, 
.git/HEAD file is generated

2. .git/HEAD file points to refs/heads/master file
Contents of refs/heads/master file is ID value,
which points to latest commit

# ======================================================================
Branch actually means file under refs/heads/ directory

Master branch is refs/heads/master file 

# ======================================================================
# Create exp branch
git branch exp

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:21:28.png

Following 2 files have been changed
- logs/refs/heads/exp
- refs/heads/exp

# ======================================================================
Click "refs/heads/exp" file

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:23:05.png

Contents of "refs/heads/exp" file point to latest commit

# ======================================================================
# To check branches
git branch
  exp
* master

# ======================================================================
# To remove branch manually
rm .git/refs/heads/exp

# To check branches
git branch
* master

# ======================================================================
# To see commits
git log

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:25:34.png

# ======================================================================
# Create exp branch manually by creating ./git/refs/heads/exp file
vim ./git/refs/heads/exp

# To check branches
git branch
  exp
* master

# ======================================================================
git checkout exp

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:27:40.png

HEAD file has been changed

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:28:04.png

Contents of HEAD file point to "refs/heads/exp"
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_12:28:51.png

Contents of "refs/heads/exp" file point to "commit"

# ======================================================================
# On exp branch, add f2.txt file
vim f2.txt
a

git add f2.txt

git commit -m "3"

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_13:38:47.png

Contents of HEAD file point to "refs/heads/exp"

Contents of "refs/heads/exp" file point to "commit 3"

# ======================================================================
# Move to mast branch
git checkout master

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_13:40:11.png

Contents of "HEAD" file point to "refs/heads/master"

Contents of "refs/heads/master" file point to "commit 2"

# ======================================================================
git log --branches --decorate -graph

https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_13:45:03.png

HEAD means current branch which you're using