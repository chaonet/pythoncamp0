# -*- coding:utf-8 -*-  
import pygame
import random
import time
#import sys
#import os
from pygame.locals import *


def scre (text):
   global screen, background
   #pygame.font.init()
   font = pygame.font.Font(None, 36)
   text = font.render(text, 1, (10, 10, 10))
   textpos = text.get_rect()
   textpos.centerx = background.get_rect().centerx
   background.blit(text, textpos)
   screen.blit(background,(0,200))
   pygame.display.flip()
   #clean background
   background.fill((250, 250, 250))
   #pygame.display.update()
   pygame.time.delay(2000)

num_random = 0


class Ai():
    def __init__(self):
       self.begin = 0
       self.end = 100

    def policy (self, result):
       if result == "begin":
          self.guess = 50
       elif result == "Higher" :
          self.end = self.guess
       elif result == "Lower" :
          self.begin = self.guess

       self.guess = int((self.begin + self.end) / 2)
       text = "(" + str(self.begin) + "+" + str(self.end) + ")/2" + "=" + str(self.guess)
       scre(text)

       return self.guess

# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    global ai_guess, num_random, screen, background, x, y
    pygame.init()
    pygame.display.set_caption("Guess number")
    screen = pygame.display.set_mode((640, 480))
    screen.fill((255,255,255))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    text_first = "New game. Range is from 0 to 100"
    scre(text_first)

    text_first = "Number of remaining guesses is 10"
    scre(text_first)

    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is 10","\n"
    pygame.time.delay(1000)
    num_random = random.randint(0, 100)
    ai_guess = Ai()
    compare ()



def compare ():
    # main game logic goes here	
    num_try = 10
    status = "begin"

    while num_try > 0 :
      guess = ai_guess.policy(status)
      text = "Guess was "+str(guess)
      scre(text)

      print "Guess was ",guess
      num_try = num_try - 1
      
      if guess > num_random:
         text = "Higher"
         scre(text)
         print "Higher"
         status = "Higher"
      elif guess < num_random:
         text = "Lower"
         scre(text)
         print "Lower"
         status = "Lower"
      else :
         text = "Correct!"
         scre(text)
         print "Correct!"
         #new_game()
         exit()
      text = "Number of remaining guess is "+str(num_try)
      scre(text)
      print "Number of remaining guess is ",num_try, "\n"
      pygame.time.delay(1000)



# call new_game 

new_game()
