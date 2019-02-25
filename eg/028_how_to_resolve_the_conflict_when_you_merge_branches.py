028_how_to_resolve_the_conflict_when_you_merge_branches

# ======================================================================
When edited files are entirely different, merging happens automatically

# ======================================================================
# Create exp branch
git branch exp

vim master.txt
a

# Let git to tract edit history of master.txt file
git add master.txt

# Take a snapshot
git commit -m "6"

# ======================================================================
# Go to exp branch from master branch
git checkout exp

vim master.txt
a

# Let git to tract edit history of exp.txt file
git add exp.txt

# Take a snapshot
git commit -m "7"

# Go to master branch from exp branch
git checkout master

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:30:40.png

current branch which you're working in is master (HEAD->master)

master branch has "commit 6"

exp branch has "commit 7"

# ======================================================================
# To merge exp branch to master branch
git merge exp

# Then, you get "merge commit"
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:32:43.png

# ======================================================================
After merge,
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:33:02.png

# ======================================================================
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:34:04.png

You can see exp.txt file after merge

Merge is simply and automatically done when you have different file

# ======================================================================
Let's try "merge" when you have files in a same file name (common.txt)

# ======================================================================
git checkout exp

vim common.txt
function a(){
}

git add common.txt

git commit -m "8"

# ======================================================================
git checkout master

git merge exp

ls -al

you will see common.txt in master branch directory

# ======================================================================
# Add 
# function b(){
# }
# into common.txt in master branch
vim common.txt
function b(){
}
function a(){
}

git commit -am "9"

# ======================================================================
git checkout exp

vim common.txt
function a(){
}
function c(){
}

git commit -am "10"

# ======================================================================
git checkout master

master branch and exp branch have edited different places 
in the same name file (common.txt)

git merge exp

# Check this file
vim common.txt
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:42:43.png

This case also can be done simply

# ======================================================================
Let's see controversy case
where multiple branches edit same places in same name file

# ======================================================================
cat common.txt
function b(){
}
function a(){
}
function c(){
}

# ======================================================================
git checkout exp

cat common.txt
function a(){
}
function c(){
}

This is because edit of "exp branch" is merged into "master branch"
but edit of "master branch" is not merged into "exp branch"

# ======================================================================
# Merge master branch into exp branch
git merge master 

cat common.txt
function b(){
}
function a(){
}
function c(){
}

# ======================================================================
git checkout master

# Edit file in master branch
vim common.txt
function b(){
}
function a(master){
}
function c(){
}

git commit -am "11"

# ======================================================================
git checkout exp

# Edit file in exp branch
vim common.txt
function b(){
}
function a(exp){
}
function c(){
}

git commit -am "12"

# ======================================================================
git checkout master

git merge exp
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:48:41.png

git status 
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:49:02.png

# ======================================================================
Let's fix conflict

# at master branch
vim common.txt
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:49:57.png

=======: delimiter

uppper part from delimiter: edit part from the branch in which you're
(in this case, it's master branch)

lower part from delimiter: edit part from the exp

- Meaning: 
Git has failed to automatically merge 2 branches,
so, user should determine what changes should be selected to continue merge
by resolving conflict

# ======================================================================
How to resolve

1. Delete upper part or lower part

2. Write new part which involves 2 functionalities
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:54:24.png

# ======================================================================
git add common.txt

git status 
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:54:50.png

git commit
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:55:20.png

git log

vim common.txt
https://raw.githubusercontent.com/youngminpark2559/vcs/master/eg/pics/2019_02_25_16:55:51.png
