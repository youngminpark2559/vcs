# ======================================================================
001_git_init

# ======================================================================
When you have a directory 
in which you want to do version mangement,
you need to let git to know that directory,
and you need to initialize that directory.

Enter that directory, and run
git init

# ======================================================================
After you run
git init

you'll get a folder named .git 

When you do version mangement,
various data like a history of changing codes, etc is generated
various data is stored in this .git folder

# ======================================================================
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

# ======================================================================
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

# ======================================================================
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

# ======================================================================
005_check_the_changed_parts_using_log_and_diff

# ======================================================================
There are 2 advantages on the created versions.

1. You can see differences on each version of project
and you can see spefic past version.

2. You can go back to a state of project

# ======================================================================
You can pass options to "git log"

# print the differences on 2 commits-based code
# using information from each commit
git log -p 

# version 4
+++ b/f1.txt
# version 3
--- a/f1.txt

+f1.txt : 2
version 4 에서의 내용

-source : 2
version 3 에서의 내용

--- /dev/null
이전 version 의 내용 : 파일이 없었음
+++ b/f2.txt
위의 version 의 다음 version 의 내용

# ======================================================================
# print all previous commits
git log hash-value-of-commit

# ======================================================================
print the difference on 2 codes
git diff hash-value-of-commit1 hash-value-of-commit2

# ======================================================================
You edit code, save code, run
git diff

then you'll see history of changes you did just ago

"git diff" is useful when you review before commit

# ======================================================================
006_go_back_to_past_code_using_reset

# ======================================================================
When latest state is "commit 5",
if you go back to "commit 3"
there are 2 ways you can use

Those 2 ways are simialar but actually are different

# ======================================================================
When you perform dangerous attemps,
to prevent side effect,
it's good to backup directory

# ======================================================================
1. reset
It's an easy way.

# When you go to "3" from "5",
# that is, you would like to remove "5" and "4" to go to "3", run
git reset hash-value-of-commit3 --hard

Even if you're heard that you remove "5" and "4",
but git generally doesn't remove data

Even if "5" and "4" look removed,
but they're actually preserved,
so that you can recover them

# ======================================================================
You can do colaborating working by using remote repository

You can share your own versioned code of remote repository to other locations 

Note that you shouldn't use "reset" after you share your versioned code

You only should use "reset" on your own code in your local PC
specifically when you don't share your code but when you work by yourself.

--hard is dangerous way,
so that there is other ways like the one using "soft"

# ======================================================================
2. revert

# ======================================================================
007_how_to_perform_add_and_writing_commit_message_and_commit_in_one_line

Every time you edit the code,
it's bothering that you should do "add, writing commit message, commit"

Try to check help on "commit" by running
git commit --help

# ======================================================================
If you use -a[or -all] option on commit after you edit or remove a file,
"add" is automatically performed
git commit -a or 

If you even want to write commit message in inline, first edit your file, and run
git commit -am "commit message"

# ======================================================================
008_how_to_use_gistory
 
# ======================================================================
pip install gistory

# ======================================================================
Move to a working directory which has .git directory and run
gistory

Copy port number and paste following address on the browser

localhost:port

Then, you will explore history contents of ".git" directory

# ======================================================================
009_mechanism_of_git_add

# ======================================================================
touch f1.txt

cat > a

# Let git to track a version history of f1.txt file
git add f1.txt

See change history via gistory

You will see "index file" has been changed

objects/78/98...85 has been added

Added objects/78/98...85 file contains contents of f1.txt file

The name of "f1.txt" file which has "a" in the file
is not contained in objects/78/98...85 file


contents a 가 담겨있는 file 이름인 f1.txt 는 위에서 added 된 file 에 담겨있지 않다
이 정보는 index file 안에 다음과 같은 format 으로 적히게 된다
7898...85 f1.txt
의미는 f1.txt file 의 contents 는 7898...85 file 에 담겨있다 이다

objects folder 안에 있는 file 을 object 라고 부른다

# ======================================================================
vim t2.txt 으로 another file f2.txt 를 create 한다
git add f2.txt 을 한다
see gistory
index file 이 변했다
objects/b6/80...46 이 created 되었다
changed index file 을 열어보면 다음과 같은 format 으로 작성되어있다
7898..85 f1.txt
b680..46 f2.txt

# ======================================================================
create a new file f3.txt which has a copied contents from f1.txt by using cp f1.txt f3.txt
and then, command git add f3.txt
and then, reload gistory
I can see 2 changed files
one is index file, and another is objects/78/98...85 which exists before but just is updated
try click and you can see contents a in it
and then try explore index file and you can see the contents of it as the following format of file shown below
7898...85 f1.txt
b680...46 f2.txt
7898...85 f3.txt

you can get the meaning of two files(f1.txt, f3.txt) indicating same object 7898...85

git manages as the same object file like a 7898...85 only if the contents is identical from two separate files even though the file names are different

no matter how you have numorous files for example 10,000 files and even if size of each file is huge, if the contents is identical in all files, git will notate only file name like f1.txt, ..., f10000.txt, those 10,000 files will indicate same object file, so that, it can prevent the probability of huge duplicate

everyone will get the same object name 7898...85 if each one would create a file with contents a in it
this is done by cryptographic hash function like SHA256

# ======================================================================
@ 지옥에서 온 GIT : 원리 - objects 파일명의 원리

# ======================================================================
contents 가 같으면 file 이 가리키는 object 의 이름이 같다

add 하면 그 파일의 contents 를 본다
contents 가 a 이면 이 정보와 몇가지 부가적 정보를 추가해서 이것을 압축한다
그리고 압축한 결과를 SHA1 처리하고 나온 hash value 로 folder 와 file 을 objects directory 안에 만든다
그리고 다시 contents a 를 그 file 안에 저장한다
그리고 index file 에 hash value(object name) 과 실제 file name f1.txt 를 connect 시켜놓는다

# ======================================================================
@ 지옥에서 온 GIT : 원리 - commit의 원리

# ======================================================================
content of file 뿐만 아니라 commit 정보(author, email, commit message) 도 objects 안의 file 에 들어간다
tree 옆에 object 가 link 되어 있다
이걸 클릭하면 해당하는 version 의 file name 과 hash value object 가 list 로 저장되어있다
445...45 f1.txt
231...27 f2.txt
445...45 f3.txt

# ======================================================================
f2 의 contents 를 수정하고 version 을 한번 더 만들어본다
git add f2.txt
그러면, index, objects 에 영향을 준다

git commit
그런다음 objects directory 를 클릭해본다
그러면 parent 와 이것이 link 를 볼수 있다
이것을 클릭하면 이 commit 의 이전 commit 을 볼 수 있다

중요한점은 첫번째 commit 과 두번째 commit 의 tree 의 hash value object link 가 다르다

첫번째 tree 를 클릭하면
445...45 f1.txt
231...27 f2.txt
445...45 f3.txt
을 볼수 있고 f2 의 object 를 클릭하면 z 라는 content 를 담고있는 file 이다

두번째 commit 의 tree 을 클릭하면 마찬가지로
445...45 f1.txt
231...27 f2.txt
445...45 f3.txt
을 볼수있고 f2 를 클릭하면 link 를 볼수있다 이 링크가 가르키는 file 은 y, z 를 저장하고 있다

commit 에는 주요한 정보 두가지가 있다
1. 이전 commit (parent)
1. commit 이 일어난 시점의 working directory 에있는 file 의 이름 f1.txt 과 이 file 의 content 를 담고있는 file 의 link 정보를 담고있다

각각의 version 마다 서로 다른 tree 를 가르키고 있다
이 tree 에는 file name(f1.txt) file 에 담겨있는 contents 를 담고있는 object 가 link 되어있다
따라서, version 에 적혀있는 tree 를 통해서 version 이 만들어진 시점의 working directory 에 대한 상태를 explore 할수있다

In other words, 각각의 version 으로 snapshot 을 만들고 이것들을 tree data structure 를 통해서 가지고 있다

# ======================================================================
objects 안에 들어가는 file(object) 은 크게 3가지이다
blob object : contents of file 을 저장한다
tree object :
34..22 f1.txt
92..93 f2.txt
34..22 f3.txt
commit object : commit 에 대한 정보를 담고있는 object

# ======================================================================
@ 지옥에서 온 GIT : 원리 - status의 원리

# ======================================================================
in a folder where there is nothing on the stage, when you execute git status,
you will see the following message "nothing to commit, working directory clean"
git 은 어떻게 nothing to commit 인지 알게되는지 알아보자

# ======================================================================
index file 을 살펴봤었다
그리고 최신 commit object 도 살펴봤다
이 둘을 비교하면 commit 할게 있는지 없는지 알 수 있다
index 에는 다음과 같은 내용이 담겨있다
28..83 d1/f1.txt
84..43 f1.txt
58..21 f2.txt
84..43 f3.txt

그리고 latest commit 을 click 해서 tree link 를 click 해 본다
28..83 d1/f1.txt
84..43 f1.txt
58..21 f2.txt
84..43 f3.txt
이런식으로 index file 의 내용과 동일하다면 commit 할 것이 없다고 판단할 수 있다

# ======================================================================
f2.txt 를 수정했다고 가정하자
그리고 add 를 하고 content of file 로 hash 하면 different value from privious hash value in the index file 가 도출된다
이전에 index file 에 저장되어있던 f2.txt 가 link 하고 있는 object link 가 다르다면 commit 할 것이 있다고 판단 할 수 있다

# ======================================================================
index 에있는
33..25 f2.txt 의 object 내용과

가장 최신 commit 에서 tree 가 가르키는 object 안의 내용에 있는
98..31 f2.txt
의 내용이 다르다면 git 은 현재 최신의 f2.txt 은 add 명령어가 사용되어 index 가 수정되었고 commit 대기 상태 이다 라는 사실을 알 수가 있다

그리고 commit 이 이루어 지면 위에서 달랐던 file 들이 동일해지면서 commit 할게 없는 상태가 된다

# ======================================================================
code 를 작업하는 working directory 에서 add 를 하면 그 내용들이 .git folder 에 있는 index file 에 등록된다
commit 을 하면 index file 에 등록된 내용이 objects 안에 저장된다
      
# ======================================================================
@ 지옥에서 온 Git - branch 만들기

# ======================================================================
git init
current directory 에 .git folder 를 포함하는 repository 가 create 된다

# ======================================================================
git commit -am "commit message"
자동으로 add commit 하는건데 한번도 add 하지 않은 file 에 이 command 를 적용하면 자동으로 add 가 되지 않는다

# ======================================================================
원래 code 를 변경하지 않으면서 client 를 위해 customizing 할때 branch 이 useful 하다

# ======================================================================
git branch : show list of branch
* master : 현재 당신이 master 라는 branch 를 쓰고 있다
git 을 사용하는 순간부터 default branch 를 사용하게 되어있는데 master 라고 불린다

# ======================================================================
git branch exp

# ======================================================================
git branch
exp
*master

current master 를 쓰고 있기때문에 * 가 master 앞에 있다

# ======================================================================
git checkout exp : exp branch 에 checkout 해서 들어간다

# ======================================================================
@ 지옥에서 온 Git - branch 정보확인

# ======================================================================
git log --branches : 현재 checkout 되어있는 branch 뿐만아니라 repository 에 있는 모든 branch 를 보여준다

git log --branches --decorate
(master) master branch 의 latest commit 을 표시한다

(HEAD -> exp)
exp 의 latest commit 이 4 임을 표시한다
HEAD : exp branch 에 checkout 되어있다

q 를 눌러서 나간다

# ======================================================================
git log --branches --decorate --graph
빨간색으로 줄이 생긴다
효용은 master branch 에서 내용이 바뀔때 줄의 효용이 생긴다

# ======================================================================
git log : 현재 branch 의 log 만 보여준다
git log --branches : 모든 branch 의 log 를 보여준다

# ======================================================================
master, exp 쭉 올라가보면 2를 담는 파일의 commit 을 만난다. 공통의 조상이다

# ======================================================================
git log --branches --decorate --graph --oneline
한줄로 간결하게 전체적으로 branch 흐름을 보여준다

# ======================================================================
source tree 깔려있으면 current directory 에서 stree 를 run 하면 current directory 가 source tree 에서 나타난다

# ======================================================================
git log master..exp
master 와 exp 의 차이가 뭐냐
matter 에는 없고 exp 에 있는걸 보여준다

# ======================================================================
git log -p master..exp
code 의 차이까지 보여준다

# ======================================================================
gid diff master..exp

# ======================================================================
@ 지옥에서 온 Git - branch 병합

# ======================================================================
master 에서 branch 했던 exp 를 작업을 하고 다시 master 로 merge 하는 방법
먼저 master 로 checkout 을 한다
그리고 git merge exp 를 한다
merge message window 에서 :wq 한다

# ======================================================================
이제 master 는 두개의 parent commit 를 갖는다
하나는 원래 master branch 의 latest commit
또 하나는 exp branch 에서의 merge 하기 직전의 latest commit

# ======================================================================
master 에 있고 exp 에 없는 것을 가져오자
git checkout exp
git merge master

# ======================================================================
exp 를 지워도 된다
git branch -d exp

# ======================================================================
@ 지옥에서 온 Git - branch 수련

# ======================================================================
branch
fast forward branch
not fast forward branch

# ======================================================================
issue 하나를 수정하기 위해 branch 를 만든다
git checkout -b iss53
다음 두 행을 -b 를 씀으로써 한번에 하는 명령어
git branch iss53 : branch iss53 create
git checkout iss53

# ======================================================================
@ 지옥에서 온 Git - stash

# ======================================================================
stash means "to hide"

When you're doing a task on a branch,
there can be a case where you need to checkout to other branch
before you finish your task on the current branch.

But it's not enough to commit "unfinished task"
but you can't checkout to other branch if you didn't do "commit"

In this situation, you can use "stash" to store (or hide) your task

# ======================================================================
git init
vim f1.txt
git add f1.txt
git commit -m 1
# branch create + checkout at the same time
git chceckout - exp 

In the middle of editing f1.txt file on the exp branch,
if you do
git 
git checkout master
edited codes on exp branch will affect master branch

# ======================================================================
# To save
git stash 

Result:
saved working directory and index state WIP on exp : 91523e45 1

# ======================================================================
# How to recover hidden task
git stash apply

# ======================================================================
# To see a list of stash
git stash list

# ======================================================================
Even if you do "git reset --hard",
if you do "git stash apply", all tasks can be recovered.

"Stash list" is always alive as long as you don't delete files explicitly

# ======================================================================
When "stash list" is multiple number of things
"git stash apply" applies most-top-stash (latest stash)

# ======================================================================
"git stash drop" removes latest stash

# ======================================================================
After you remove latest stash,
git stash apply; git stash drop;

# ======================================================================
git stash 로 임시저장하고
git stash apply; git stash drop; 으로 적용하고 삭제할수 있다
한번에 하려면 git stash pop 을 쓴다

# ======================================================================
add 하지 않아서 tracked 되지 않고 있는 file 에 대해서는 stash 를 쓸 수 없다

# ======================================================================
@ 지옥에서 온 Git - 원리 : merge & conflict

# ======================================================================
git checkout -b exp : exp branch 만들면서 동시에 chceckout 까지 한다

master, exp branch 에서 같은 부분을 수정했다고 가정한다

in master, git merge exp : exp 것들 master 로 합친다
그런데 conflict 되어 auto merge failed

# ======================================================================
go to gistory
index file 을 보면
xx1 1 f1.txt
xx2 2 f1.txt
xx3 3 f1.txt

이런식으로 conflict 가 occurred 하면 xx 뒤에 숫자가 붙는다
각각을 click 해 본다
1번인 f1.txt
는 내용이 common 이다
수정전에 공통으로 가지고 있었던 f1.txt 의 내용이다

xx2 2 f1.txt 를 click 해본다
master 로 수정된 내용을 볼 수 있다

xx3 3 f1.txt 를 click 해본다
병합이 될 대상인 exp 내용이 써져있다

이러한 3가지 정보를 바탕으로 3 way merge 라는 merge 가 이루어질 수 있다

# ======================================================================
MERGE_HEAD 를 click 해 본다
merge 가 될 대상(exp) 의 latest commit 이다

# ======================================================================
MERGE_MSG 는 merge 를 하는 과정에서 conflict 가 발생했는데 commit 을 할 때 보여줄 message 이다

# ======================================================================
ORIG_HEAD 는 merge 는 위험한 작업이라서 그 이전으로 돌아가기 위한 일종의 back up 이다

# ======================================================================
objects/34/xx4 는 충돌이 일어난 내용을 설명하는 file 이다

# ======================================================================
merge 를 해주는 tool 이 있다
여기서는 kdiff3 를 사용해본다

git config --global merge.tool kiff3 를 해서 merge command 를 했을 때 kdiff3 가 실행되도록 한다
beyondcompare tool 을 쓴다면 git config --global merge.tool bc 를 하면 된다

# ======================================================================
git mergetool 은 conflict file 에 대해서 mergetool 을 이용해서 merge 하도록 git 에게 commnad 한다

# ======================================================================
kiff3 의 layout 은 다음과 같다
4칸으로 구분됨
왼쪽은 f1.txt(base) 이다
가운데는 f1.txt(local) 이다
오른쪽은 f1.txt(remote) 이다
밑에는 output directory 이다

# ======================================================================
conflict 란 다음과 같다
common parent commit 이 있다
여기에서 master, exp branch 가 같은 곳을 수정하고 각각 commit 을 했다
이 둘은 수정내용은 다르지만 common parent commit 이 있다는 것이고 이것을 base 라고 부른다
local 은 checkout 되어 merge 되는 내용을 받는 쪽이다

A,B,C 를 누르면 각각 common, master, exp 가 채택되어 merge 된다
동시에 누를수도있다
다 누르면 common, master, exp 내용 전부다 merge 된다

master.exp 같은 내용으로 아래 칸에서 직접 수정할 수 도있다

그리고 저장한다

# ======================================================================
@ 지옥에서 온 Git - 원리 : 3 way merge

# ======================================================================
2way merge : base 는 보지 않고 me, other 만 비교하여 merge 하는 방법이다
3way merge : base 를 참고하여 me, other 을 merge 하는 방법이다

# ======================================================================
<table border=1>
  <tr>
    <th>me</th>
    <th>other</th>
    <th>2way merge</th>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td>conflict</td>
  </tr>
  <tr>
    <td>B</td>
    <td>B</td>
    <td>B</td>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>conflict</td>
  </tr>
  <tr>
    <td></td>
    <td>D</td>
    <td>conflict</td>
  </tr>
</table>

1, 2 같이 다른 경우는 auto merge 할때 뭐가 맞는지 알 수 없다
그래서 merger 에게 뭐가 맞는지 conflict 를 내야한다
공백, D 경우 내용이 없는게 수정된 사항인지 있는게 수정된 사항인지 알 수 없다

# ======================================================================
<table border=1>
  <tr>
    <th>me</th>
    <th>base</th>
    <th>other</th>
    <th>3way merge</th>
  </tr>
  <tr>
    <td>A</td>
    <td>A</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>B</td>
    <td>B</td>
    <td>B</td>
  </tr>
  <tr>
    <td>1</td>
    <td>C</td>
    <td>2</td>
    <td>conflict</td>
  </tr>
  <tr>
    <td></td>
    <td>D</td>
    <td>D</td>
    <td></td>
  </tr>
</table>

AA공백이면 me 는 수정하지 않았고 other 은 수정했다라는걸 알수있으므로 수정한것을 채택할 수 있다
세명이 같으므로 B
셋 모두 다르므로 conflict 를 낸다
공백DD 이므로 수정된 사항이 있음을 인지하고 이를 반영한다

# ======================================================================
@ 지옥에서 온 Git - 원격 저장소 소개

# ======================================================================
remote repository(ex, github, private common server), local repository

# ======================================================================
remote repository : backup, coworking

# ======================================================================
@ 지옥에서 온 Git - 원격 저장소 생성

# ======================================================================
git init --bare name-of-repository 은 작업은 할수없고 그냥 repository 역할만 할수 있는 option 이다
remote repository 를 만들때 사용한다

# ======================================================================
git remote add address-of-remote-repository 는 local repository 와 remote repository 를 연결한다
경로를 길게 쓰기 번거로우므로 origin 을 사용하면 주의의 alias 가 된다
git remote add origin address-of-remote-repository

add 된 repository 를 지우고 싶으면 git remote remove origin 을 사용한다

# ======================================================================
현재 local repository 에서 master branch 상태이다
git push 를 하면 master branch 의 내용을 remote repository 에 똑같은 이름의 branch 로 push 한다

push 방식(matching, simple 중에서)을 global 하게 설정하려면 git config --global push.default simple 을 사용한다

# ======================================================================
git push --set-upstream origin master 은 push 할때 origin 주소에 master branch 로 push 한다
--set-upstream 을 써주면 앞으로 master branch 에서 push 를 하면 자동으로 origin 의 master 로 push 하도록 설정하는 것이다

# ======================================================================
@ 지옥에서 온 Git - github 소개 (Github)

# ======================================================================
clone 방법
원하는 directory 로 이동한다
git clone address-of-remote-repository 하면 folder 가 생성되면서 clone 된다
혹은 git clone address-of-remote-repository folder-name 으로 folder 를 직접 만들면서 할 수 있다

# ======================================================================
clone 한 folder 에서 git log 하면 commit history 를 볼 수 있다

git log --reverse 를 하면 거꾸로 log 를 볼 수 있다

첫번째 commit 의 code 를 보려면 commit hash value 를 copy 하고 q 로 나가서 git checkout commit-hash-value 를 하면 된다
그러면 current branch 가 이 commit 이 된다

그리고 ls -al 로 file 목록을 본다

# ======================================================================
@ 지옥에서 온 Git - 원격 저장소 만들기 (Github)

# ======================================================================
두가지 상황이 있을 수 있다

상황1 : remote repository 를 만들고 이것을 clone 해서 local repository 를 만들고 여기에서 작업을 하는 방식
상황2 : local repository 에서 작업을 해왔다. 그리고 작업 내역을 remote repository 로 push 하고 싶을때

# ======================================================================
상황2부터 보자
git remote add origin https://github.com/youngmtool/test.git
현재 local repository 에 remote repository (origin https://github.com/youngmtool/test.git) 를 연결(add) 시킨다

# ======================================================================
git 은 여러개의 remote repository 를 하나의 local repository 에 연결시킬 수 있다
loca repository 에서 작업한걸 A or B 등으로 마음대로 push 할 수 있다

기본 branch 의 alias 가 master 인 것 처럼, origin 은 local repository 와 연결되어 있는 가장 기본적인 remote repository 의 alias 로 사용된다

# ======================================================================
git 에서는 local repository 를 기준으로 얘기한다

내가 작업하는 local repository 에서 remote repository 로 작업을 보낼때 push 라고 표현한다

git push -u origin master 는 현재 checkout 되어있는 local repository 의 branch 의내용을 origin 에 해당하는 remote repository 의 master branch 에 push 한다는 의미이다

-u 는 한번만 쓰면 되는 option 으로서 local repository 의 branch 와 remote repository 의 master branch 를 서로 연결 시켜서 다음부터는 git push 만 쓰면 자동으로 위와 같이 push 되게 하는 option 이다

# ======================================================================
위의 방법은 작업하고 있던 local repository 를 remote repository 로 옮기는 방식이며 backup 의 의미를 갖는다

# ======================================================================
먼저 remote repository 에 자료가 있고 이걸 local repository 로 clone 방법은
원하는 folder 로 이동한 뒤
git clone address . 을 하면 되고, dot 을 써주면 현재 directory 를 가리킨다

# ======================================================================
@ 지옥에서 온 Git - 동기화 방법 (Github)

# ======================================================================
clone 을 git_home, git_office 두 군데에 해본다

git commit --amend 는 commit message 를 수정할 수 있다
remote repository 에 올리기 전에만 하는게 좋다

# ======================================================================
git_home 에서 수정하고 remote repository 에 push 한다

# ======================================================================
git_office 에서 (local repository 입장에서) remote repository 에 있는 내용을 pull 을 한다

# ======================================================================
@ 지옥에서 온 Git - tag 1 (기본 사용법)

# ======================================================================
github 에 release : source code 에서 사용자들에게 제공되어도 되는 각각의 의미있는 version 들을 모아놓은 곳이다

v2.12.0
e8e394 

release version v2.12.0 에 해당하는 commit version 은 e8e394 이다

# ======================================================================
commit 을 할 때마다 master branch 의 latest commit 은 바뀌어야한다

v2.12.0
e8e394 

이와 같은 version commit 은 바뀌면 안된다

# ======================================================================
tag 은 언제나 똑같은 commit 을 가르킨다
branch 는 항상 바뀐다

# ======================================================================
현재 master 에서 xx1 을 가리키고 있다고 가정한다
이때, git tag 하면 1.0.0 version 이 tag 된다

이러한 방식은 light weight tag 이다

# ======================================================================
tag 에 대한 정보를 포함하고 싶을때는
annotated tag 를 다음과 같이 쓴다
git tag -a 1.1.0 -m "bug fix"

# ======================================================================
git tab -v 1.1.0 을 치면 detailed information 이 나온다

# ======================================================================
git push --tags 는 push 할 때 tag 정보도 같이 push 한다
그럼 github 에 release 가 생긴다
github 에서는 edit tag 를 할 수 도 있다

# ======================================================================
tag 를 삭제하는 방법
git tag -d 1.1.0

# ======================================================================
@ 지옥에서 온 Git - tag 2 (원리)

# ======================================================================
git tag 1.1.2

refs/tags/1.1.2 file 이 만들어진다
link 가 있다
click 하면 관련된 commit 이다

# ======================================================================
직접 tag file 만들기
go to refs/tags
create 1.1.3 file
contents should be commit hash value

# ======================================================================
annotated tag 는 addionally file 이 만들어진다
여기에 상세정보가 들어있다
