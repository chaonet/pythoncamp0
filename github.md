新建一个资源


拷贝

添加`.md`的文件

### 引用issue
同一仓库的issue
commit message里面使用 #加上issue号 ，比如`#8`, github会自动关联`issue 8`跟这个commit. 

其他仓库的issue
要链接到其他仓库的Issue，就使用`user_name/repo_name#ISSUE_NUMBER`的方式，例如tiimgreen/toc#12。

### 关闭issue
随着commit关闭一个issue,在confirm merge的时候可以使用以下命令来关闭相关issue:
```
fix #xxx
fixes #xxx
fixed #xxx
close #xxx
closes #xxx
closed #xxx
```

提交pull请求

[GitHub秘籍，为你解读Git与Github酷而少知的功能] (http://www.xuanfengge.com/github-cheats.html)
