004_git_stage_area

# ======================================================================
# Copy fi.txt and create f2.txt from fi.txt
cp fi.txt f2.txt

# You let git to tract version history on f2.txt file
git add f2.txt

# ======================================================================
Why should you do "add" than "commit"
after you edit a source file?

As you're editing the source file,
there can be case where you loss "commit timing"

It's ideal that a single commit contains a single edit.

In this context, 
if you loss "commit timing",
a single commit can contain large edit.

In this situation, 
you can commit only several files which you want to commit
by using "add"

# ======================================================================
Let's perform "add" on one f1.txt file out of 2 files

After "add", you will see message saying
"changes to be commited"

And you also will see "modified" colored by green

You will see messag saying 
"changes not staged for commit"

You will see "modified" colored by red

In this state, if you run
commit
f1.txt file will be involved in the new version project.

f2.txt file will not be involved in that new version project.

It means you can selectively commit files by using "git add"

# ======================================================================
Status where "add" is applied, 
state before commit (which is to take a snapshot of the code on a stage)
is called "stage area"

# ======================================================================
The results from "commit" are stored in "repository"