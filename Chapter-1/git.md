#### git是什么，为什么要git
git，是一个分布式的版本控制器

分布式，就是每一个参与编辑的终端都有一个完整的本地拷贝，可以直接进行编辑，而不一定要连上一个特定的服务器。这样可以方便多人协同做项目，而且有多处备份

版本控制，所做的每一次改动，git都会有一个日志记录下是谁在什么时候做了什么改动，并且每个改动都会自动做备份，以便需要时候回退

#### 安装git
通过在终端输入“git”，可以知道系统有没有安装git

>chao@ubuntu:~$ git --version

>git version 1.9.1

如果没有，输入命令`sudo apt-get install git`就可以进行安装

#### 初始化，建立仓库（repository）
仓库就是一个被git控制的目录，git可以记录目录下所有文件的修改、删除，甚至可以还原   
仓库可以通过在一个空目录下，通过命令“git init”对目录进行初始化，然后git会在这个目录下新建一个隐藏的目录`.git`

>chao@ubuntu:~/test$ git init

>初始化空的 Git 版本库于 /home/chao/test/.git/

>chao@ubuntu:~/test$ ls

>chao@ubuntu:~/test$ dir

>chao@ubuntu:~/test$ ls -a

>.  ..  .git

>chao@ubuntu:~/test$ dir -a

>.  ..  .git

对版本进行控制、记录的文件都在这个文件夹中  
也可以通过命令`git clone url`克隆其他地方的库过来

>chao@ubuntu:~/test$ git status

>位于分支 master

>初始提交

>无文件要提交（创建/拷贝文件并使用 `git add` 建立跟踪）

#### 暂存区、工作区


#### 新建文件
这时git还没有办法记录、跟踪这个文件的改动

>chao@ubuntu:~/test$ vi hello.txt

>chao@ubuntu:~/test$ ls

>hello.txt

>chao@ubuntu:~/test$ git status

>位于分支 master

>未跟踪的文件:

>  （使用 "git add <file>..." 以包含要提交的内容）

>

>	hello.txt

>

>提交为空，但是存在尚未跟踪的文件（使用 "git add" 建立跟踪）

#### 暂存、提交
注意：所有的版本控制器只能跟踪文本文件改动，包括git。对于二进制文件，比如word，无法跟踪文件的变化。

第一步：在仓库下`git add xx.txt`，对仓库中准备提交的变更进行暂存，就是放入暂存区

>chao@ubuntu:~/test$ git add hello.txt

>chao@ubuntu:~/test$ git status

>位于分支 master

>要提交的变更：

>  （使用 "git reset HEAD <file>..." 撤出暂存区）

>

>	新文件:       hello.txt

第二步：对暂存区的变更进行提交`git commit`，如果没有`add`进行暂存，通常就没办法提交。不过也有办法，后面会说到

>chao@ubuntu:~/test$ git commit -m "add file'hello.txt'"

>[master 8cdb9e4] add file'hello.txt'

> 1 file changed, 1 insertion(+)

> create mode 100644 hello.txt

>chao@ubuntu:~/test$ git status

>位于分支 master

>无文件要提交，干净的工作区

`git commit`后面的选项`-m`用来对这次提交的更改进行描述，这个描述会被记录下来。

手动删除进行跟踪的文件后，提交时会提示变更没有暂存

>chao@ubuntu:~/test$ git status

>位于分支 master

>尚未暂存以备提交的变更：

>  （使用 "git add/rm <file>..." 更新要提交的内容）

>  （使用 "git checkout -- <file>..." 丢弃工作区的改动）

>

>	删除:         hello.txt

>	删除:         hellohello.txt

>	删除:         hi.txt

>修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）

使用 -a 选项，不`add`，强行暂存并提交修改

>chao@ubuntu:~/test$ git commit -a -m "delete all files"

>[master 6567dba] delete all files

> 3 files changed, 6 deletions(-)

> delete mode 100644 hello.txt

> delete mode 100644 hellohello.txt

> delete mode 100644 hi.txt

可以连续`add`几次，然后用一条`commit`提交

也可以使用通配符跟踪某一类型的所有文件`add *.txt`

#### 查看具体的修改信息
修改仓库中的文件"hi.txt"

>hello!


>hi!
>boys and girls.

`git diff`查看被修改过，但还没有被缓存、提交的文件里，改动的内容

>chao@ubuntu:~/test$ git diff hello.txt
>diff --git a/hello.txt b/hello.txt
>index 4effa19..1bc3c3d 100644
>--- a/hello.txt
>+++ b/hello.txt
>@@ -1 +1,2 @@
>-hello!
>+hi!
>+boys and girls.

知道做了什么修改以后，可以选择放弃当前工作区的改动，还是放到暂存区准备提交

>chao@ubuntu:~/test$ git status
>位于分支 master
>尚未暂存以备提交的变更：
>  （使用 "git add <file>..." 更新要提交的内容）
>  （使用 "git checkout -- <file>..." 丢弃工作区的改动）
>
>	修改:         hello.txt

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）

>chao@ubuntu:~/test$ git add hello.txt
>chao@ubuntu:~/test$ git commit -m "modify hello.txt"
>[master 906b1d7] modify hello.txt
> 1 file changed, 2 insertions(+), 1 deletion(-)

>chao@ubuntu:~/test$ git status
>位于分支 master
>无文件要提交，干净的工作区

#### 放弃修改
"git checkout -- <file>..." 丢弃工作区的改动

#### 版本回退
还真的能回退！太强大！所有版本的内容都被保存下来了。

- `git log`查看库中所有`提交的历史`，从最近一个版本变动开始显示

>chao@ubuntu:~/test$ git log

>commit 906b1d7ed397f80d310adf9bd44f3331d4501f9e
>Author: chao <chao@ubuntu.com>
>Date:   Tue Mar 17 21:06:22 2015 +0800
>
>    modify hello.txt
>
>commit 8cdb9e4a1fffbe7a2ad3a99a3ab9a6a6af4bf17b
>Author: chao <chao@ubuntu.com>
>Date:   Tue Mar 17 20:54:13 2015 +0800
>
>    add file'hello.txt'
>
>commit 6567dba9e0f55d9d335273c94b12dc433e1ad81b
>Author: chao <chao@ubuntu.com>
>Date:   Tue Mar 17 20:46:16 2015 +0800
>
>    delete all files
>
>commit 2f9b22c60b068e2904cbfddb1d39686c66aae5a4
>Author: chao <chao@ubuntu.com>
>Date:   Tue Mar 17 20:31:56 2015 +0800
>
>    modify hi.txt
>
>commit b6d9b3b345ff891e42d31b8bffd32986a69294ed
>Author: chao <chao@ubuntu.com>
>Date:   Tue Mar 17 20:22:29 2015 +0800
>
>    add file'hi.txt'
>
>commit 7837360f48214cf2dc494627880bdd0c3a061305
>Author: 超 <chao@ubuntu.ubuntu-domain>
>Date:   Tue Mar 17 10:35:43 2015 +0800
>
>    modify hello.txt
>
>commit 9b21e1b0a1451124fb6d271b0ee0282f25b4b57d
>Author: 超 <chao@ubuntu.ubuntu-domain>
>Date:   Tue Mar 17 10:12:31 2015 +0800
>
>    add world!
>
>commit fe5d031a42594c58868372b4459989365cdf4fc8
>Author: 超 <chao@ubuntu.ubuntu-domain>
>Date:   Mon Mar 16 21:39:43 2015 +0800
>
>    add file'hellohello.txt'
>
>commit 0a4750519d2f4966fa4016590da82ee9c26f67db
>Author: 超 <chao@ubuntu.ubuntu-domain>
>Date:   Mon Mar 16 21:09:53 2015 +0800
>
>    add file'hello.txt'
>(END)

可以查看简略信息

>chao@ubuntu:~/test$ git log --pretty=oneline

>906b1d7ed397f80d310adf9bd44f3331d4501f9e modify hello.txt

>8cdb9e4a1fffbe7a2ad3a99a3ab9a6a6af4bf17b add file'hello.txt'

>6567dba9e0f55d9d335273c94b12dc433e1ad81b delete all files

>2f9b22c60b068e2904cbfddb1d39686c66aae5a4 modify hi.txt

>b6d9b3b345ff891e42d31b8bffd32986a69294ed add file'hi.txt'

>7837360f48214cf2dc494627880bdd0c3a061305 modify hello.txt

>9b21e1b0a1451124fb6d271b0ee0282f25b4b57d add world!

>fe5d031a42594c58868372b4459989365cdf4fc8 add file'hellohello.txt'

>0a4750519d2f4966fa4016590da82ee9c26f67db add file'hello.txt'

- `git reflog`用来记录你的`命令历史`，前面的一串数字就是`commit id`的前七位

>chao@ubuntu:~/test$ git reflog

>906b1d7 HEAD@{0}: commit: modify hello.txt

>8cdb9e4 HEAD@{1}: commit: add file'hello.txt'

>6567dba HEAD@{2}: commit: delete all files

>2f9b22c HEAD@{3}: commit: modify hi.txt

>b6d9b3b HEAD@{4}: commit: add file'hi.txt'

>7837360 HEAD@{5}: commit: modify hello.txt

>9b21e1b HEAD@{6}: commit: add world!

>fe5d031 HEAD@{7}: commit: add file'hellohello.txt'

>0a47505 HEAD@{8}: commit (initial): add file'hello.txt'

- 两种回退方法：

需要确定想退回到哪个版本。  
1. 在Git中，用`HEAD`表示当前版本，上一个版本是`HEAD^`，上上一个版本就是`HEAD^^`  
`git reset --hard HEAD^`

2. 也可以用`commit id`的前7位确定版本`
`git reset --hard 3628164`


查看当前hello.txt的内容

>chao@ubuntu:~/test$ cat hello.txt

>hi!

>boys and girls.

退回到前一个版本

>chao@ubuntu:~/test$ git reset --hard HEAD^

>HEAD 现在位于 8cdb9e4 add file'hello.txt'

>chao@ubuntu:~/test$ cat hello.txt

>hello!

退回到文件都被删除版本

>chao@ubuntu:~/test$ git reset --hard 6567dba

>HEAD 现在位于 6567dba delete all files

>chao@ubuntu:~/test$ ls

还原到最后的版本

>chao@ubuntu:~/test$ git reset --hard 906b1d7

>HEAD 现在位于 906b1d7 modify hello.txt

>chao@ubuntu:~/test$ ls

>hello.txt

>chao@ubuntu:~/test$ cat hello.txt

>hi!

>boys and girls.

#### 远程仓库
可以使用一台电脑作为 git 服务器，专门用来存放仓库，谁需要用，就从仓库克隆到自己的电脑进行使用，github 就是这样一个免费的仓库托管服务器。

那么，怎么使用远程仓库？

##### 从自己的 github 中克隆已有的仓库到本地
进入自己的 github 中想要克隆的仓库，在右边有`clone URL`，并且有几种 clone 方式可以选择：`You can clone with HTTPS, SSH, or Subversion. `，点击URL右边的复制按钮，复制URL

在本地仓库目录下，敲入命令`git clone <URL>`，就可以将这个仓库从 github 克隆到本地

那么，`HTTPS, SSH, or Subversion`这些方式有有什么区别呢？

git 支持多个协议进行文件传输，为了确认你有权限对仓库进行修改操作，需要验证身份。`HTTPS`方式比较麻烦，每次传输文件（克隆、提交、拉取），都需要输入用户名和密码。而`SSH`方式，可以在第一次配置完成后，以后都不需要再输入用户名及密码。

##### 将本地仓库推送到 github 进行托管
在 github 新建一个空仓库`exam`，复制clone的URL
将本地仓库`test`推送到 github 的`exam`

本地仓库`test`下git的配置文件

[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true

用git remote 将 `exam` 的URL与一个自定义的主机名相关联，并将关联写配置文件



git remote add [-t <分支>] [-m <master>] [-f] [--tags|--no-tags] [--mirror=<fetch|push>] <名称> <url>


，将内容复制到本地，并将修改后的内容保存到 github 呢
首先，要将本地的指定 git 仓库和 github 的特定仓库建立关联，这样以后执行的的推送、拉取命令，才知道是对哪些库进行的操作

git remote add

git pull

git push -u origin master



#### 分支
新建分支可以理解为创立一个做子项目的平行世界，分支之间可以彼此独立存在，进行暂存、提交，当子项目完成，进行分支合并，子项目就成了主项目的一部分。类似一个复杂设备，分成几个部分，独立进行安装，最后组合成一个整体。
chao@ubuntu:~/test$ git status
位于分支 master


#### 设置用于记录的用户信息

>chao@ubuntu:~/test$ git commit -m "modify hello.txt"

>[master 7837360] modify hello.txt

> Committer: 超 <chao@ubuntu.ubuntu-domain>

>您的姓名和邮件地址基于登录名和主机名进行了自动设置。请检查它们正确

>与否。您可以通过下面的命令对其进行明确地设置以免再出现本提示信息：

>

>    git config --global user.name "Your Name"

>    git config --global user.email you@example.com

>

>设置完毕后，您可以用下面的命令来修正本次提交所使用的用户身份：

>

>    git commit --amend --reset-author

>

> 1 file changed, 2 insertions(+), 1 deletion(-)

>chao@ubuntu:~/test$ git config --global user.name "chao"

>chao@ubuntu:~/test$ git config --global user.email chao@ubuntu.com


#### 帮助：

`git --help`查看常用命令

`git help <命令>`查看指定的命令

#### Q&A
1. 使用git add和直接新建有什么区别？

>两个不同的概念，git add只是将文件放到暂存区，准备提交，并不是新建一个文件并记录

工作区和暂存区分别是做什么用的？

2. remote add和push的区别？是否remote add是可以添加指定文件，而push是完整更新替换？

git push -u origin master简化命令，怎么简化的？

3. git中origin master是可变参数还是规定的名称？

4. 分支的作用是什么？如果是备份，不是已经有版本回退功能了么？

5. 分支不可以做到两个分支同时独立发展，最终合并么？

6. 分支应该如何使用比较好？

7. 为什么我从本地推送到github没有说要用ssh，好像用的https，SSH不是必须的吧？难道是我没有推成功？
