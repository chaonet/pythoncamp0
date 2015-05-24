作业:
注册并使用了gitbook
期待:
激发创作一本书的欲望
尝试将内容加进书目中
第一时间发布图书
指标:
入门: 注册并登录了gitbook
中阶: 新建了gitbook图书,并且通过git命令更改的内容
高阶: 自如的调整目录和内容,安装了 DISQUS 插件
天才: 定制自己的样式,本地随时发布 kindle 版本给小伙伴们
教程:
什么是 gitbook?
为什么 gitbook?
gitbook 类似工具/平台有什么?!
对比其它 gitbook 优点/问题是什么?
你使用 gitbook 的技巧?
怎么改进 gitbook?

#### GitBook平台
可以发布通过GitBook命令行工具制作的电子书。

发布到GitBook平台后，默认是以静态网站的形式在线生成、显示电子书，可以在电子书的首页选择下载，有三种格式；PDF、ePub、Mobi三种格式可以选择。

#### 注册GitBook
打开GitBook：https://www.gitbook.com/
点击“Sign up for GitBook”
可以选“Sign in with GitHub”，将GitHub和GitBook进行关联
也可以直接输入用户名、密码

一本书至少要有“README.md”和“SUMMARY.md”文件

电子书的首页会使用“README”文件的内容作为内容简介。

电子书的目录章节结构是通过“SUMMARY”文件定义的。
```
# Summary

* [Part I](part1/README.md)
    * [Writing is nice](part1/writing.md)
    * [GitBook is nice](part1/gitbook.md)
* [Part II](part2/README.md)
    * [We love feedback](part2/feedback_please.md)
    * [Better tools for authors](part2/better_tools.md)
```

GitBook默认支持Markdown语法编辑的文件

可以通过将喜欢的电子书封面JPEG图片命名为“cover.jpg”并更新到GitBook进行更改，最大尺寸1800x2360。

配置电子书：
所有对电子书的配置都保存在一个名为“book.json”的文件中，可以使用JSON语法编辑。
plugins插件
`{ "plugins": ["disqus"] }`
pluginsConfig
```
{
  "plugins": ["disqus"],
  "pluginsConfig": {
    "disqus": {
      "shortName": "chaonet"
    }
  }
}
```

#### 定制格式
修改“book.json”
```
{
    "styles": {
        "website": "styles/website.css",
        "ebook": "styles/ebook.css",
        "pdf": "styles/pdf.css",
        "mobi": "styles/mobi.css",
        "epub": "styles/epub.css"
    }
}
```

#### 创建新书
选择“GitHub”，直接从关联的GitHub账号导入资源
选择“Basic”的电子书:以“start writing”直接开始写，GitBook会初始化一个最简单的电子书结构，生成“README.md”“SUMMARY.md”并需要编辑；在本地创建资源或对已有资源，通过git推送到GitBook；“link to github”，关联指定的github资源，并从gitbook直接对资源进行编辑。



#### 发布书
在本地用GitBook命令行工具对电子书资源进行编译，将md文件编译为GitBook平台支持的html格式文件。

#### 推送历史
“Book History”，可以看到发布电子书的历史记录，每条后面的勾表示发布成功。

#### 与GitHub关联
“GitHub Repository”，填写需要关联的GitHub资源信息，“ 用户名/资源名”

#### 选择/定制着陆页面样式
“landing page”，

#### 邮件发送更新消息
“Personal settings”，“Profile”，“Emails”，可以选择向注册邮箱发送GitBook的日报和更新信息等邮件。

#### 编辑
1. 在本地进行编辑，并用git进行推送更新
2. 在GitBook进入电子书，点击`Edit Book`直接进行编辑

#### 调整章节目录结构
1. 在本地修改“SUMMARY.md”文件，并用`$ gitbook build ./`编译，自动创建新目录结构
2. “Edit book”，在“Table of Contents”右击章节，可以选择“Add Section”、“Edit”、“Remove”，可以同样右击页面进行操作。

#### 更改插件
“Edit book”，点击右上角的倒三角，“Add Plugin”，查找并添加插件。

#### 域名、链接
电子书主页：http://{user_name}.gitbooks.io/{book_name}/
电子书内容链接：http://{user_name}.gitbooks.io/{book_name}/content/

#### 查看
`View Book`

#### 电子书Git URL
“Opions”，“Publication”，“Git URL”，使用git push进行发布和更新时使用的URL

“Once you delete a repository, there is no going back. Please be certain.”删除这个电子书


