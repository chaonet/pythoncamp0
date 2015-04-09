- 自学课程:https://class.coursera.org/interactivepython2-002/lecture
    + Week 6a Classes
    + Week 6b Tiled images
- 唯一作业:
    + 猜数游戏AI版
- 期待:
    + 抽象你的自然思维
    + 在尽可能短的代码行数中完成:无人介入的猜数游戏
    + 最好能动画式演示游戏过程　　　//2. 还在折腾ｐｙｇａｍｅ
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
"import pygame"    imports the package with all the available Pygame modules. 
import os, sys　import the standard "os" and "sys" python modules. These allow us to do things like create platform independent file paths.
from pygame.locals import *　　　　optional, and puts a limited set of constants and functions into the global namespace of your script. 
There is a special pygame module named "locals". This module contains a subset of pygame. The members of this module are commonly used constants and functions that have proven useful to put into your program's global namespace. This locals module includes functions like "Rect" to create a rectangle object, and many constants like "QUIT, HWSURFACE" that are used to interact with the rest of pygame. Importing the locals module into the global namespace like this is entirely optional. If you choose not to import it, all the members of locals are always available in the pygame module.


"pygame.init()"       initializes each of these modules.checks through the imported pygame modules and attempts to initialize each one of them. 

black = 0, 0, 0   颜色用RGB color定义

"pygame.display.set_mode()"    create a graphical window

 load our ball image. Pygame supports a variety of image formats through the SDL_image library, including JPG, PNG, TGA, and GIF. The "pygame.image.load()" function returns us a Surface with the ball data. 
 
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

