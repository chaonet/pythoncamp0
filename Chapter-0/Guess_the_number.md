#### 需要的编程知识：


#### 最初构思的程序结构
按钮：实现随机数的生成、开始新游戏

文本框：输入猜测值

后台：函数进行判断，打印出比较的结果

次数限制

然后发现Coursera上老师给了一个文本框、两个按钮调用的函数、一个`new_game`的函数……

#### 重新构思
`new_game`的函数用于首次运行

两个按钮分别调用0~100、0~1000的函数

这三个函数都调用对文本的判断

#### 最终确定结构
仔细看了课程中老师的代码隐藏的行数，彻底推翻原先的程序结构

推测出`new_game`为主程序，开始时由全局定义的`num_range`确定默认随机数范围0~100

然后由两个按钮进行对`num_range`的重新赋值并传递给`new_game`

最终由`new_game`调用文本框执行判断

#### 内容调整
`range100`和`range1000`的代码最先确定

然后开始考虑尝试次数如何生成，想到了公式 N*3+1，N为`0`的个数，但如何实现呢？

想起引入的`math`模块还没使用，查阅了文档，找到`math.log()`函数

然后纠结`new_game`和`input_guess`之间随机数的传递

后来通过同时定义`global num_random`完成

接下来是剩余次数的改变，由于需要每触发一次文本就减一，所以想到用一个新变量`n`进行累加，并用剩余次数减去`n`

同样必须在`new_game`和`input_guess`同时定义`n`

priint时，最后加`,"\n"`进行换行

#### 有待完善的地方
转换：转换成次数时，不知为什么，产生的是浮点数，使用int()进行转换，1000转换失败

10.0依次减一，1.0之后显示的却不是0.0

尝试次数归零后，还不能强行终止

[代码：Guess_the_number]