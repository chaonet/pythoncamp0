- 自学课程:https://class.coursera.org/interactivepython2-002/lecture
    + Week 6a Classes
    + Week 6b Tiled images
- 唯一作业:
    + 猜数游戏AI版
- 期待:
    + 抽象你的自然思维
    + 在尽可能短的代码行数中完成:无人介入的猜数游戏
    + 最好能动画式演示游戏过程　　　//2. 勉强算是成功了
- 要求:
    + 基础: 用程序模拟出自己猜数的策略, 并进行检验    //1. ｏｋ
    + 可用: 用自制的猜数AI, 和自己的游戏对战　  //3. 整合ＡＩ和之前的文本输入
    + 合格: 猜数AI的游戏过程,可记录,可回放　　　//4. 还是列表
    + 天才: 猜数AI的游戏过程,可记录,可回放,可分享,加载...进一步的:　　　//5. 分享，需要输出为文件，加载，需要读取文件
        * 通过大量的游戏对战,统计自个儿AI 的能力?! 
        * 发布他人的AI 也可以接入的服务?　　　　　//单人ｏｒ多人切换，提供接入接口
        * 并行多组游戏?
        * 怎么证明自个儿的 AI 策略是最优的?能用最少次数猜中?
- 教程期待:
    + 向 6个月 前看过以往自己教程的自己认真描述
    + 怎么设计代码来减少行数完成这个任务?
    + 有哪些理解上的坑,如何能理解之?

代码
import pygame    导入包中所有有效的ｐｙｇａｍｅ模块
import os, sys　导入标准的 "os" 和 "sys" python 模块． These allow us to do things like create platform independent file paths.
from pygame.locals import *　　　　可选，optional, and puts a limited set of constants and functions into the global namespace of your script. 
There is a special pygame module named "locals". This module contains a subset of pygame. The members of this module are commonly used constants and functions that have proven useful to put into your program's global namespace. This locals module includes functions like "Rect" to create a rectangle object, and many constants like "QUIT, HWSURFACE" that are used to interact with the rest of pygame. Importing the locals module into the global namespace like this is entirely optional. If you choose not to import it, all the members of locals are always available in the pygame module.


pygame.init()      检查导入的模块，并初始化

black = 0, 0, 0   ｐｙｇａｍｅ默认用ＲＧＢ三元组定义颜色颜色

pygame.display.set_mode()    创建一个绘画窗口

pygame.image.load()　　　 load our ball image. Pygame supports a variety of image formats through the SDL_image library, including JPG, PNG, TGA, and GIF. The "" function returns us a Surface with the ball data. 
 
actually update the visible display
When we are finished drawing we call the "pygame.display.flip()" method. This makes everything we have drawn on the screen Surface become visible. 

Create The Background
background = pygame.Surface(screen.get_size())       creates a new surface for us that is the same size as the display window
background = background.convert()
background.fill((250, 250, 250))        Fill takes an RGB triplet as the color argument.

Put Text On The Background, Centered
we must create the font object and render it into a new surface. We then find the center of that new surface and blit (paste) it onto the background.
font = pygame.font.Font(None, 36)   The font is created with the font module's Font() constructor. Usually you will pass the name of a truetype font file to this function, but we can also pass None, which will use a default font. The Font constructor also needs to know the size of font we want to create
text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))    render that font into a new surface. The render function creates a new surface that is the appropriate size for our text. 
textpos = text.get_rect(centerx=background.get_width()/2)    find the centered position of the text on our display. We create a "Rect" object from the text dimensions, which allows us to easily assign it to the screen center.
background.blit(text, textpos)    blit (blit is like a copy or paste) the text onto the background image

Main Loop
while 1:
    clock.tick(60)      call to our clock object, which will make sure our game doesn't run faster than 60 frames per second.
    
pygame.display.flip()    flip() the contents of pygame's software double buffer to the screen. This makes everything we've drawn visible all at once.

Game Over


http://www.pygame.org/docs/tut/intro/intro.html

pygame.display.update()    when we finish drawing to the screen, we call pygame.display.update() which will show everything we've drawn onto the screen.


pygame.time.get_ticks	—	get the time in milliseconds
pygame.time.wait	—	pause the program for an amount of time
pygame.time.delay	—	pause the program for an amount of time
pygame.time.set_timer	—	repeatedly create an event on the event queue
pygame.time.Clock	—	create an object to help track time


from pygame.color import THECOLORS
pygame.draw.circle(screen,THECOLORS["red"],[100,100],30,0)

pygame.draw.rect()用来创建一个矩形。Rect(left,top,width,height)用来定义位置和宽高，具体代码如下：
pygame.draw.rect(screen,[255,0,0],[250,150,300,200],0)

import pygame,sys
import time
import random

render(text, antialias, color, background=None) -> Surface

   text ：要显示的文字内容,仅支持单行，即不能使用\n进行换行，如要打印多行，要建立多个font对象。

问题１：
  File "guess_the_number_ai.py", line 36, in new_game
    num_random = random.randrange(0, 100)
AttributeError: 'builtin_function_or_method' object has no attribute 'randrange'

用错
from random import *
少了
import random

问题２：
窗口弹出然后自动关闭，怎么才能一直打开？
程序结束自动关闭，加个延迟？
＞在每个输出文字的地方加了pygame.time.delay(600)

问题３：
Traceback (most recent call last):
  File "guess_the_number_ai.py", line 70, in <module>
    pygame.draw.rect(screen, (0,0,0), (10, 10, 300, 400), width=0)
TypeError: rect() takes no keyword arguments


问题４：
chao@ubuntu:~/pythoncamp0/source/part3$ python guess_the_number_ai.py
New game. Range is from 0 to 100
Number of remaining guesses is 10 

Guess was 50
Lower
Number of remaining guess is 9 

Guess was 75
Lower
Number of remaining guess is 8 

Guess was 87
Lower
Number of remaining guess is 7 

Guess was 93
Lower
Number of remaining guess is 6 

Guess was 96
Lower
Number of remaining guess is 5 

Guess was 98
Lower
Number of remaining guess is 4 

Guess was 99
Lower
Number of remaining guess is 3 

Guess was 99
Lower
Number of remaining guess is 2 

Guess was 99
Lower
Number of remaining guess is 1 

Guess was 99
Lower
Number of remaining guess is 0 
猜不到１００，改一下随机数范围

问题５：
pygame.display.set_caption("Guess number")

screen = pygame.display.set_mode((640, 480))

screen.fill((255,255,255))
挪到上面，然后加了pygame.display.flip()
窗口设定的白色就出现了，否则是黑色，ｗｈｙ？

问题６：
    global ai_guess, num_random, text, textpos, background
    
    pygame.draw.rect(screen,[255,0,0],[250,150,300,200],3)
    text = font.render("New game. Range is from 0 to 100", 1, (10, 10, 10)) 
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    screen.blit(background,(0,0))

字贴不上去

函数外的内容：
```
import pygame
import random
import time

pygame.init()

pygame.font.init()

pygame.display.set_caption("Guess number")

screen = pygame.display.set_mode((640, 480))

screen.fill((255,255,255))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

font = pygame.font.Font(None, 36)

text = font.render("Hello!", 1, (10, 10, 10))

textpos = text.get_rect()

textpos.centerx = background.get_rect().centerx

background.blit(text, textpos)

screen.blit(background,(0,0))

pygame.display.flip()
```
只显示了Hello!

放到函数里面？定义一个函数，专用于显示动画
不行，可能需要调整程序结构，一个主函数，在里面定义，然后分别调用几个功能子函数

问题７：
Traceback (most recent call last):
  File "guess_the_number_ai.py", line 97, in <module>
    pygame.display.flip()
pygame.error: video system not initialized


问题８：
Traceback (most recent call last):
  File "guess_the_number_ai.py", line 116, in <module>
    new_game()
  File "guess_the_number_ai.py", line 71, in new_game
    screen("Number of remaining guesses is 10")
TypeError: 'pygame.Surface' object is not callable


问题９：
将 pygame.display.set_caption("Guess number")放到主程序里面以后

  File "guess_the_number_ai.py", line 56
    pygame.display.set_caption("Guess number")
                                             ^
IndentationError: unindent does not match any outer indentation level

问题１０：
scre(text_first1,x,y)
文字自动重叠，怎么换行，刷新？

问题１１：
输入框


