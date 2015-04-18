### 需求：
在本地运行 CodeSkulptor 上编写的交互程序

### 问题：
需要安装哪些模块  
这些模块的作用是什么  
到哪里下载  
如何安装  
怎么使用  

### 寻找软件,模块
+ CodeSkulptor是什么?
CodeSkulptor 是一个基于浏览器的 Python 翻译器，被用于在线课程 “An Introduction to Interactive Programming in Python”.  
CodeSkulptor 为交互式编程提供了 SimpleGUI 模块，但这个模块只能在 CodeSkulptor 使用 , pygame 和 tkinter 是 python 中交互式编程通用的模块．  
[课程中的说明](http://www.codeskulptor.org/demos.html#tabs-Demos)  

+ 要实现某项功能，python需要的软件包列表可以在下面的网址搜索  
[链接](https://pypi.python.org/pypi)

+ 搜索'simplegui'  
SimpleGUICS2Pygame 01.09.00  
[结果页面](https://pypi.python.org/pypi?%3Aaction=search&term=simplegui&submit=search)  

### 软件的下载和安装

#### SimpleGUICS2Pygame
+ 是一个可以实现 CodeSkulptor(一个开源项目，能够让 python 程序直接在浏览器中运行) 中 SimpleGUI 功能的 python 模块．包括在原生的 python 中运行 CodeSkulptor 中编写的程序．
+ 下载源代码或安装程序
[python.org](https://pypi.python.org/pypi/SimpleGUICS2Pygame) or [bitbucket.org](https://bitbucket.org/OPiMedia/simpleguics2pygame)

+ 在 ubuntu 下安装SimpleGUICS2Pygame

下载 'SimpleGUICS2Pygame-?.tar.gz', 随便解压到哪个目录,　进入解压后的出现的文件夹`SimpleGUICS2Pygame-?/',　用管理员权限进行安装
```
$ tar zxvf SimpleGUICS2Pygame-01.09.00.tar.gz
$ cd SimpleGUICS2Pygame-01.09.00/
$ sudo python setup.py install
```

+ 其他需要安装的软件
    - 模块 'simpleplot' 需要安装 [matplotlib](http://matplotlib.org/) (并且必须另外单独安装).
    - 模块 'simplegui_lib' (以及它的子模块) 和 'simpleguics2pygame' (除了Timer class) 需要安装 [Pygame](http://www.pygame.org/) (并且必须另外单独安装).

+ 检查所有软件是否安装成功
可以运行小程序[SimpleGUICS2Pygame_check.py](https://bitbucket.org/OPiMedia/simpleguics2pygame/src/default/SimpleGUICS2Pygame/script/) 

只安装了pygame
```
$ python SimpleGUICS2Pygame_check.py
script/SimpleGUICS2Pygame_check.py (April 21, 2014)
===================================================
python - version 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2]


import matplotlib ok - Version 1.4.3


import pygame ok - Version 1.9.1release
pygame.init() 6 modules loaded ok


import SimpleGUICS2Pygame FAILED! No module named SimpleGUICS2Pygame

import SimpleGUICS2Pygame.codeskulptor FAILED! No module named SimpleGUICS2Pygame.codeskulptor
import SimpleGUICS2Pygame.codeskulptor_lib FAILED! No module named SimpleGUICS2Pygame.codeskulptor_lib
import SimpleGUICS2Pygame.numeric FAILED! No module named SimpleGUICS2Pygame.numeric
import SimpleGUICS2Pygame.simplegui_lib FAILED! No module named SimpleGUICS2Pygame.simplegui_lib
import SimpleGUICS2Pygame.simplegui_lib_draw FAILED! No module named SimpleGUICS2Pygame.simplegui_lib_draw
import SimpleGUICS2Pygame.simplegui_lib_fps FAILED! No module named SimpleGUICS2Pygame.simplegui_lib_fps
import SimpleGUICS2Pygame.simplegui_lib_keys FAILED! No module named SimpleGUICS2Pygame.simplegui_lib_keys
import SimpleGUICS2Pygame.simplegui_lib_loader FAILED! No module named SimpleGUICS2Pygame.simplegui_lib_loader
import SimpleGUICS2Pygame.simpleguics2pygame FAILED! No module named SimpleGUICS2Pygame.simpleguics2pygame
import SimpleGUICS2Pygame.simpleplot FAILED! No module named SimpleGUICS2Pygame.simpleplot
```

三个模块都安装完成
```
$ python SimpleGUICS2Pygame_check.py
script/SimpleGUICS2Pygame_check.py (April 21, 2014)
===================================================
python - version 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2]


import matplotlib ok - Version 1.4.3


import pygame ok - Version 1.9.1release
pygame.init() 6 modules loaded ok


import SimpleGUICS2Pygame ok - Version 01.09.00

import SimpleGUICS2Pygame.codeskulptor ok
import SimpleGUICS2Pygame.codeskulptor_lib ok
import SimpleGUICS2Pygame.numeric ok
import SimpleGUICS2Pygame.simplegui_lib ok
import SimpleGUICS2Pygame.simplegui_lib_draw ok
import SimpleGUICS2Pygame.simplegui_lib_fps ok
import SimpleGUICS2Pygame.simplegui_lib_keys ok
import SimpleGUICS2Pygame.simplegui_lib_loader ok
import SimpleGUICS2Pygame.simpleguics2pygame ok
import SimpleGUICS2Pygame.simpleplot ok
```

+ 相关链接
    - [simpleguics2pygame网站](http://simpleguics2pygame.readthedocs.org/en/latest/)
    - [simpleguics2pygame代码库](https://bitbucket.org/OPiMedia/simpleguics2pygame)

+ 使用
```
只需将
`import simplegui`
改为
`import SimpleGUICS2Pygame.simpleguics2pygame as simplegui`
就可以在标准的 Python 中，使用这个模块 (和 Pygame)运行CodeSkulptor 里面编写的程序.
```

+ SimpleGUICS2Pygame软件包, 包含的模块及作用
    - codeskulptor — 替换CodeSkulptor 中的 codeskulptor 模块
    - codeskulptor_lib — 一些其他的方法
    - numeric — 替换 CodeSkulptor 中的 numeric 模块
    - simplegui_lib — 用来导入下面列出的模块
    - simplegui_lib_draw — 绘画方法
    - simplegui_lib_fps — 计算显示每秒刷新的帧
    - simplegui_lib_keys — 管理键盘事件的帮助类／函数
    - simplegui_lib_loader —  加载图像和声音的类
    - simpleguics2pygame — 主模块, 替换 CodeSkulptor 中的 simplegui 模块
    - simpleplot — 替换 CodeSkulptor 中的 simpleplot 模块

[原文链接](https://simpleguics2pygame.readthedocs.org/en/latest/modules.html)

#### matplotlib
matplotlib 是python最著名的绘图库，它提供了一整套和matlab相似的命令API，十分适合交互式地行制图。而且也可以方便地将它作为绘图控件，嵌入GUI应用程序中。
[下载](http://matplotlib.org/downloads.html)

安装

`$ tar zxvf matplotlib-1.4.3.tar.gz`
`$ sudo python setup.py install`

#### pygame
+ 什么是Pygame
Pygame是 跨平台 Python模块，专为电子游戏设计。

+ 下载
[官网链接](www.pygame.org)

[下载页面](http://www.pygame.org/download.shtml)
选择'Unix Distributions'中的'Ubuntu'
根据系统版本选择'trusty (14.04LTS)'
在最下面的'下载 python-pygame'根据CPU,选择'i386'

选择了'kr.archive.ubuntu.com/ubuntu'
点击后自动下载"python-pygame_1.9.1release+dfsg-9ubuntu1_i386.deb"文件

+ 安装

双击,在软件中心安装

验证安装是否成功
```
$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:38) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import pygame
>>> print pygame.ver
1.9.1release
>>> 
```

+ Q&A

pygame和SimpleGUICS2Pygame有什么区别或者关联？
>SimpleGUICS2Pygame是一个python包, 使用Pygame来运行在CodeSkulptor上编写的代码