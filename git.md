git，是一个分布式的版本控制器
分布式，就是每一个参与编辑的终端都有一个完整的本地拷贝，可以直接进行编辑，而不一定要联网
版本控制，所做的每一次改动，git都会有一个日志记录下是谁在什么时候做了什么改动

#### 安装：
通过在终端输入“git”，可以知道系统有没有安装git
chao@ubuntu:~$ git --version
git version 1.9.1
如果没有，输入命令`sudo apt-get install git`就可以进行安装

#### 仓库（repository）
仓库就是一个被git控制的目录，git可以记录目录下所有文件的修改、删除，甚至可以还原？？
仓库可以通过在一个空目录下，通过命令“git init”对目录进行初始化，然后git会在这个目录下新建一个隐藏的目录`.git`
【
chao@ubuntu:~/test$ git init
初始化空的 Git 版本库于 /home/chao/test/.git/
chao@ubuntu:~/test$ ls
chao@ubuntu:~/test$ dir
chao@ubuntu:~/test$ ls -a
. .. .git
】
对版本进行控制、记录的文件都在这个文件夹中
也可以通过命令`git clone url`克隆其他地方的库过来
【
chao@ubuntu:~/test$ git status
位于分支 master

初始提交

无文件要提交（创建/拷贝文件并使用 `git add` 建立跟踪）
】

#### 新建文件，这时git还没有办法跟踪记录这个文件
【
chao@ubuntu:~/test$ vi hello.txt
chao@ubuntu:~/test$ ls
hello.txt
chao@ubuntu:~/test$ git status
位于分支 master

初始提交

未跟踪的文件:
（使用 "git add <file>..." 以包含要提交的内容）

hello.txt

提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）
】

#### 准备提交、提交。
注意：所有的版本控制器只能跟踪文本文件改动，包括git。但对于二进制文件，比如word，无法跟踪文件的变化。
第一步：在仓库下`git add xx.txt`，做提交准备
【
chao@ubuntu:~/test$ git add hello.txt
chao@ubuntu:~/test$ git status
位于分支 master

初始提交

要提交的变更：
（使用 "git rm --cached <file>..." 撤出暂存区）

新文件: hello.txt
】
第二步：提交变更记录`git commit`
【
chao@ubuntu:~/test$ git commit -m "add file'hello.txt'"  
[master （根提交） 0a47505] add file'hello.txt'  
Committer: 超 <chao@ubuntu.ubuntu-domain>  
您的姓名和邮件地址基于登录名和主机名进行了自动设置。请检查它们正确  
与否。您可以通过下面的命令对其进行明确地设置以免再出现本提示信息：  
  
git config --global user.name "Your Name"  
git config --global user.email you@example.com  
  
设置完毕后，您可以用下面的命令来修正本次提交所使用的用户身份：  
  
git commit --amend --reset-author  
  
1 file changed, 1 insertion(+)  
create mode 100644 hello.txt
】
`git commit`后面的选项`-m`用来对这次提交的更改进行说明，这个说明会被记录下来。

>可以连续`add`几次，然后用一条`commit`提交
>也可以使用通配符跟踪某一类型的所有文件`add *.txt`

#### 查看具体的修改信息
`git diff`

#### 取消跟踪记录

#### 分支
chao@ubuntu:~/test$ git status
位于分支 master

#### 查看版本变动信息

#### 操作用户信息的设置

remote add和push的区别？是否remote add是可以添加指定文件，而push是完整更新替换？

#### 帮助：
`git --help`查看常用命令
`git help <命令>`查看指定的命令

#### Q&A
使用git add和直接新建有什么区别？
>两个不同的概念，git add只是对已经有的文件进行预提交，准备记录变化，并不是新建一个文件并记录






