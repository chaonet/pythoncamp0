git，是一个分布式的版本控制器
分布式，就是每一个参与编辑的终端都有一个完整的本地拷贝，可以直接进行编辑，而不一定要联网
版本控制，所做的每一次改动，git都会有一个日志记录下是谁在什么时候做了什么改动

#### 安装：
通过在终端输入“git”，可以知道系统有没有安装git
chao@ubuntu:~$ git --version
git version 1.9.1
如果没有，输入命令`sudo apt-get install git`就可以进行安装

#### 初始化，建立仓库（repository）
仓库就是一个被git控制的目录，git可以记录目录下所有文件的修改、删除，甚至可以还原？？  
仓库可以通过在一个空目录下，通过命令“git init”对目录进行初始化，然后git会在这个目录下新建一个隐藏的目录`.git`
【
chao@ubuntu:~/test$ git init
初始化空的 Git 版本库于 /home/chao/test/.git/
chao@ubuntu:~/test$ ls
chao@ubuntu:~/test$ dir
chao@ubuntu:~/test$ ls -a
.  ..  .git
chao@ubuntu:~/test$ dir -a
.  ..  .git
】
对版本进行控制、记录的文件都在这个文件夹中  
也可以通过命令`git clone url`克隆其他地方的库过来
【
chao@ubuntu:~/test$ git status
位于分支 master

初始提交

无文件要提交（创建/拷贝文件并使用 `git add` 建立跟踪）
】

#### 新建文件
这时git还没有办法记录、跟踪这个文件的改动
【
chao@ubuntu:~/test$ vi hello.txt
chao@ubuntu:~/test$ ls
hello.txt
chao@ubuntu:~/test$ git status
位于分支 master
未跟踪的文件:
  （使用 "git add <file>..." 以包含要提交的内容）

	hello.txt

提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
】

#### 暂存、提交
注意：所有的版本控制器只能跟踪文本文件改动，包括git。对于二进制文件，比如word，无法跟踪文件的变化。
第一步：在仓库下`git add xx.txt`，对仓库中准备提交的变更进行暂存，就是放入暂存区
【
chao@ubuntu:~/test$ git add hello.txt
chao@ubuntu:~/test$ git status
位于分支 master
要提交的变更：
  （使用 "git reset HEAD <file>..." 撤出暂存区）

	新文件:       hello.txt

】
第二步：对暂存区的变更进行提交`git commit`，如果没有`add`进行暂存，通常就没办法提交。不过也有办法，后面会说到
【
chao@ubuntu:~/test$ git commit -m "add file'hello.txt'"
[master 8cdb9e4] add file'hello.txt'
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
chao@ubuntu:~/test$ git status
位于分支 master
无文件要提交，干净的工作区
】
`git commit`后面的选项`-m`用来对这次提交的更改进行描述，这个描述会被记录下来。

手动删除进行跟踪的文件后，提交时会提示变更没有暂存
chao@ubuntu:~/test$ git status
位于分支 master
尚未暂存以备提交的变更：
  （使用 "git add/rm <file>..." 更新要提交的内容）
  （使用 "git checkout -- <file>..." 丢弃工作区的改动）

	删除:         hello.txt
	删除:         hellohello.txt
	删除:         hi.txt

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）

使用 -a 选项，不`add`，强行暂存并提交修改
chao@ubuntu:~/test$ git commit -a -m "delete all files"
[master 6567dba] delete all files
 3 files changed, 6 deletions(-)
 delete mode 100644 hello.txt
 delete mode 100644 hellohello.txt
 delete mode 100644 hi.txt

>可以连续`add`几次，然后用一条`commit`提交
>也可以使用通配符跟踪某一类型的所有文件`add *.txt`

#### 查看具体的修改信息
修改仓库中的文件"hi.txt"
>hello!
` 
>hi!
>boys and girls.

`git diff`查看被修改过，但还没有被缓存、提交的文件里，改动的内容
chao@ubuntu:~/test$ git diff hello.txt
diff --git a/hello.txt b/hello.txt
index 4effa19..1bc3c3d 100644
--- a/hello.txt
+++ b/hello.txt
@@ -1 +1,2 @@
-hello!
+hi!
+boys and girls.

知道做了什么修改以后，可以选择放弃当前工作区的改动，还是放到暂存区准备提交
【
chao@ubuntu:~/test$ git status
位于分支 master
尚未暂存以备提交的变更：
  （使用 "git add <file>..." 更新要提交的内容）
  （使用 "git checkout -- <file>..." 丢弃工作区的改动）

	修改:         hello.txt

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
】

【
chao@ubuntu:~/test$ git add hello.txt
chao@ubuntu:~/test$ git commit -m "modify hello.txt"
[master 906b1d7] modify hello.txt
 1 file changed, 2 insertions(+), 1 deletion(-)
chao@ubuntu:~/test$ git status
位于分支 master
无文件要提交，干净的工作区
】

#### 取消跟踪记录

#### 分支
chao@ubuntu:~/test$ git status
位于分支 master

#### 查看版本变动信息

#### 设置用于记录的用户信息
【
chao@ubuntu:~/test$ git commit -m "modify hello.txt"
[master 7837360] modify hello.txt
 Committer: 超 <chao@ubuntu.ubuntu-domain>
您的姓名和邮件地址基于登录名和主机名进行了自动设置。请检查它们正确
与否。您可以通过下面的命令对其进行明确地设置以免再出现本提示信息：

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

设置完毕后，您可以用下面的命令来修正本次提交所使用的用户身份：

    git commit --amend --reset-author

 1 file changed, 2 insertions(+), 1 deletion(-)
】

chao@ubuntu:~/test$ git config --global user.name "chao"
chao@ubuntu:~/test$ git config --global user.email chao@ubuntu.com


#### 帮助：
`git --help`查看常用命令
`git help <命令>`查看指定的命令

#### Q&A
使用git add和直接新建有什么区别？
>两个不同的概念，git add只是对已经有的文件进行预提交，准备记录变化，并不是新建一个文件并记录

>remote add和push的区别？是否remote add是可以添加指定文件，而push是完整更新替换？

>git origin master是可变参数还是规定的名称？
