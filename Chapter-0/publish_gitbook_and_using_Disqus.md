### GitBook和GitBook平台
GitBook是一个电脑上的一个命令行工具，可以使用GitHub/Git和Markdown制作漂亮的电子书。

电脑本地使用gitbook工具对资源中的章节结构和”.md”文件进行编译，然后可以将本地的电子书推送到在线的GitBook平台公开发布。
https://www.gitbook.com/

### 安装和使用GitBook

+ 安装npm（Node Package Manager）

`$ sudo apt-get install npm`

会安装一堆软件包，然后提示有软件包需要升级，问是否希望继续执行，当然选Y。然后npm就安装好了

+ 安装GitBook

`$ sudo npm install gitbook -g`

+ 创建GitBook电子书
    - 使用GitBook制作电子书，必备两个文件：README.md和SUMMARY.md。README.md是电子书的内容简介，SUMMARY.md用来定义电子书章节结构

    - 有两种方法:1. 用已有的SUMMARY.md 文件内容，通过 gitbook init 自动生成目录结构，添加.md文件进行编译；2. 对已有的资源，编辑SUMMARY.md 文件，然后编译、运行。

    - 我们因为已经在GitHub有了资源，所以只介绍第二种。
    
    - 将GitHub的资源pull下来，添加 SUMMARY.md 文件，描述 GitBook 目录结构
```
# SUMMARY

  * [缘起](begin.md)
  * [注册并使用了gitbook](Chapter-0/github_and_gitbook.md)
  * [git发布私人图书](Chapter-0/git.md)
  * [Markdown 教程](Chapter-0/Markdown.md)
  * [Mailling-List 教程](Chapter-0/Mailling-List.md)
  * [Github 教程](Chapter-0/github.md)
  * [部署gitbook](Chapter-0/gitbook.md)
  * [IIPPy-part1:Guess_the_number](Chapter-0/Guess_the_number.md)
  * [进击 IIPPy-part2]
    * [可回放的点彩画板](Chapter-1/Drawing_board.md)
```
+ 编译GitBook

开始编译

`$ gitbook build ./`

报错，提示“/usr/bin/env: node: 没有那个文件或目录”

搜了一下，按这个链接的方法添加目录索引：https://github.com/joyent/node/issues/3911

`$ sudo ln -s /usr/bin/nodejs /usr/bin/node`

再试编译，提示想要使用 gitbook command，需要卸载gitbook ，安装 'gitbook-cli'
```
$ gitbook build ./
You need to install 'gitbook-cli' to have access to the gitbook command anywhere on your system.
If you've installed this package globally, you need to uninstall it.
>> Run 'npm uninstall -g gitbook' then 'npm install -g gitbook-cli'
```
卸载gitbook
```
chao@ubuntu:~/pythoncamp0$ sudo npm uninstall -g gitbook
unbuild gitbook@2.0.1
```
安装gitbook-cli

`$ sudo npm install -g gitbook-cli`

再进行编译
```
$ sudo gitbook build ./
info: loading book configuration....
warn: you should specify a gitbook version to use in your book.json, for example: 2.x.x 
info: OK 
info: >> 0 plugins loaded 
info: start generation with website generator 
info: clean website generator
info: OK 
info: generation is finished 

Done, without error
```
在资源仓库里生成了一个”_book”文件夹，按原始的目录结构创建文件夹，在每一个文件夹下包含对原有“.md”文件编译后生成的“.html”版本，”_book”文件夹里就是在gitbook上看到的目录和文件。

之前是直接将没有编译的资源推送到GitBook平台，资源中只有.md文件，导致打开后提示“404”，无法正常发布。

+ 运行

在本地用浏览器观察推送到GitBook后,打开页面的效果

打开”_book”文件夹，右键运行里面的html文件，就可以在本地看到发布到GitBook上的效果

+ 将电子书同步到GitHub进行备份，并在GitBook平台发布

通过 git status、git add 和 git commit 命令添加对新增/修改的提交。

用git push 完成将资源同步到GitHub和GitBook平台。


### Disqus
如果希望别人能够在自己发布到GitBook平台的电子书文章下评论，可以使用第三方评论工具Disqus

+ 注册disqus

打开:https://disqus.com/

点击"Sign Up",输入邮箱,用户名,密码,创建账号

这是第一步

+ 新建站点

登录后,点击右上角的齿轮,选择"Add Disqus To Site",填写"Site name",这是book.json里面要填的"shortName","Finish  registration".

> "shortName"和注册时填写的用户名作用不同: 用户名是账号的名称,而"shortName"是这个新建站点唯一的名称.一个账号可以有多个站点,也就有多个"shortName".

> 在网页上使用这个"shortName"以后,这个网页下面的所有评论都会发送到disqus上对应"shortName"的站点. 打开网页时,"shortName"告诉disqus需要加载并显示哪个站点的评论.

> 一个站点可以包含多个页面的讨论内容.

+ 安装disqus

有了"shortName"以后, 开始最后一步: 插件安装

点击主页右上角的齿轮,选择"Admin","Settings"

点击"Settings"标签下的"Install",disqus给出了几种网站平台的安装指引,选择对应图标,进入安装指引界面,按步骤操作.

没有针对gitbook的安装指引,   可以使用下面的方式进行安装

```
$ npm install gitbook-plugin-disqus
npm http GET https://registry.npmjs.org/gitbook-plugin-disqus
npm http 304 https://registry.npmjs.org/gitbook-plugin-disqus
gitbook-plugin-disqus@0.0.1 ../node_modules/gitbook-plugin-disqus
```
配置仓库里的“book.json”文件，将disqus集成到GitBook电子书

添加下面的内容
```
{
  "plugins": ["disqus"],
  “pluginsConfig”: {
  "disqus": {
   “shortName":” “NAME-FROM-DISQUS”
    }
}
}
```
将NAME-FROM-DISQUS 改为在DISQUS 的用户名

编译，提示加载了“gitbook-plugin-disqus”插件
```
$ sudo gitbook build ./
info: loading book configuration....
warn: you should specify a gitbook version to use in your book.json, for example: 2.x.x 
info: OK 
info: load plugin gitbook-plugin-disqus ....OK 
info: >> 1 plugins loaded 
info: start generation with website generator 
info: clean website generator
info: OK 
info: generation is finished 

Done, without error
```
这时候，GitBook对电子书里所有”html”的文件都做了修改，打开时会加载plugins 。

通过 git status、git add 和 git commit 命令添加对新增/修改的提交。

用git push 完成将资源同步到GitHub和GitBook平台。

打开gitbook页面，Disqus评论框出现了。顺便试了一下，真的可以评论。

然后登录Disqus，可以看到评论

+ 管理站点

点击主页右上角的齿轮,选择"Admin"

"Comments"中可以对当前站点里的评论进行处理,比如删除.

"Discussions"可以对指定页面下的讨论进行处理,比如关闭评论.

"Settings"-"Advanced"-"Trusted Domains",因为在网页上使用"shortName"向disqus发送评论不需要验证身份,为了防止有人用你的"shortName",可以添加信任的网站,只接收这些网站发来的评论.


+ 删除站点

"Admin",点左上角的三道横线,选择要删除的站点,"Settings"-"Advanced"-"Delete from Disqus",点击"Delete site and comments"按钮,删除当前站点.


### 参考资料
http://www.ituring.com.cn/article/127645

https://github.com/GitbookIO/gitbook

http://my.oschina.net/waylau/blog/355179

http://www.waylau.com/about-gitbook/
