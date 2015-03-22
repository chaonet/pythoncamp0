# Markdown
## 标题
- 多个`#`，越多字号越小

\# 标题

\## 标题

\### 标题

\#### 标题

\##### 标题

\###### 标题

\####### 标题

# 标题
## 标题
### 标题
#### 标题
##### 标题
###### 标题

- 标题下`=`或者`-`

标题  
\-

标题
-

## 超链接
\[连接](https://github.com/chaonet/Markdown/edit/master/README.md)

[连接](https://github.com/chaonet/Markdown/edit/master/README.md)

## 图片
右击图片，`复制图片网址`，获得url  
!\[图片](url)

![自定义](https://avatars2.githubusercontent.com/u/11154448?v=3&s=96)

## 目录索引
[索引](#link)  


## 底纹
\`底纹`(键盘左上角的“~”)

`底纹`

## 特殊字符转义
特殊字符前，加`\`

破坏原有字符的组合结构就可以了

## 引用、嵌套引用、段落引用
\>引用1

\>>引用2

>引用1
>>引用2



## 换行
换(两个空格+回车)行

换  
行

换（两个回车）行

换

行

## 列表
无序列表使用`*`、`+`或是`-`作为列表标记，标记符号后空一格

顶格，前面是黑点；缩进一格，前面是白点

\* Red

* Red

 * Red

\+  Red

+  Red

 +  Red

\-  Red

-  Red

 -  Red

有序列表  
数字接着一个英文句点，接着一个空格

1. Bird
2. McHale
3. Parish

## 目录索引

<a name="link"></a>
#### 索引

## 表格

名称 | 性别 | 年龄

\--- | --- | ---

表格1 | 表格2 | 表格3

表格4 | 表格5 | 表格6

名称 | 性别 | 年龄
--- | --- | ---
表格1 | 表格2 | 表格3
表格4 | 表格5 | 表格6

## 分割线
三个或者更多`-`,`*`,`_`

\---

---

\***

***

\___

___

## 加粗、倾斜
- 倾斜

\*倾斜*

*倾斜*

\_倾斜_

_倾斜_

- 加粗

\*\*加粗**

**加粗**

\__加粗__

__加粗__

- 删除线

\~~删除线~~

~~删除线~~

- 加粗和倾斜

\*\*加粗和\_加粗倾斜_**

**加粗和_加粗倾斜_**

\_\_加粗和\*加粗倾斜*__

__加粗和*加粗倾斜*__

## 没有超链接的注脚
Text prior to footnote reference.[^2]

[^2] Comment to include in footnote.

## 代码区块
最上和最下一行输入 3 个 `

\`\`\`  
代  
码  
区  
块  
\`\`\`

```
代
码
区
块
```

### 语法高亮
\```ruby

require 'redcarpet'

markdown = Redcarpet.new("Hello World!")

puts markdown.to_html

\```

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

[参考资料1](http://help.gitbook.com/format/markdown.html)

[参考资料2](https://help.github.com/articles/github-flavored-markdown/)

### END
