#### GitBook和GitBook平台
GitBook是一个电脑上的一个命令行工具，可以使用GitHub/Git和Markdown制作漂亮的电子书。

电脑本地使用gitbook工具对资源中的章节结构和”.md”文件进行编译，然后可以将本地的电子书推送到在线的GitBook平台（https://www.gitbook.com/）公开发布。

#### 安装和使用GitBook
+ 安装npm（Node Package Manager）
`$ sudo apt-get install npm`

会安装一堆软件包，然后提示有软件包需要升级，问是否希望继续执行，当然选Y。然后npm就安装好了

+ 安装GitBook
`$ sudo npm install gitbook -g`

+ 创建GitBook电子书
    使用GitBook制作电子书，必备两个文件：README.md和SUMMARY.md。README.md是电子书的内容简介，SUMMARY.md用来定义电子书章节结构

    有两种方法:1. 用已有的SUMMARY.md 文件内容，通过 gitbook init 自动生成目录结构，添加.md文件进行编译；2. 对已有的资源，编辑SUMMARY.md 文件，然后编译、运行。

    我们因为已经在GitHub有了资源，所以只介绍第二种。
    
    将GitHub的资源pull下来，添加 SUMMARY.md 文件，描述 GitBook 目录结构
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
打开”_book”文件夹，右键运行里面的html文件，就可以在本地看到发布到GitBook上的效果

##### 将电子书同步到GitHub进行备份，并在GitBook平台发布
通过 git status、git add 和 git commit 命令添加对新增/修改的提交。

用git push 完成将资源同步到GitHub和GitBook平台。


##### Disqus
如果希望别人能够在自己发布到GitBook平台的电子书文章下评论，可以使用第三方评论工具Disqus

安装disqus插件
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

在gitbook打开页面后，提示

`“We were unable to load Disqus. If you are a moderator please see our troubleshooting guide.”`

点入排错指南

“https://help.disqus.com/customer/portal/articles/472007-i-m-receiving-the-message-%22we-were-unable-to-load-disqus-%22”

因为只修改了shortname，所以只看这一段：

“Your shortname is missing or incorrect”

“Disqus won't load if you haven't yet registered a forum shortname or if the shortname you have entered is incorrect. ”

原来是还没有注册论坛昵称

点进链接“https://disqus.com/admin/create/”

在“Site name”填写，内容就是之前填写的“NAME-FROM-DISQUS”，完成注册

再次加载gitbook页面，Disqus评论框出现了。顺便试了一下，真的可以评论。


然后登录Disqus，可以看到评论

##### 参考资料
http://www.ituring.com.cn/article/127645

https://github.com/GitbookIO/gitbook

http://my.oschina.net/waylau/blog/355179

http://www.waylau.com/about-gitbook/
