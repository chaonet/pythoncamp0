import pygame
import random
import time
#import sys
#import os
#from pygame.locals import *



pygame.init()

pygame.display.set_caption("Guess number")

screen = pygame.display.set_mode((640, 480))

screen.fill((255,255,255))

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
       return self.guess

# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    global ai_guess, num_random
    
    pygame.draw.rect(screen,[255,0,0],[250,150,300,200],3)
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
      print "Guess was",guess
      num_try = num_try - 1
      
      if guess > num_random:
         print "Higher"
         status = "Higher"
      elif guess < num_random:
         print "Lower"
         status = "Lower"
      else :
         print "Correct!"
         #new_game()
         exit()
      print "Number of remaining guess is",num_try, "\n"
      pygame.time.delay(1000)


# create frame

pygame.display.flip()
#pygame.time.delay(1000)
#clock.tick(60) 

#pygame.quit()

# register event handlers for control elements and start frame


# call new_game 

new_game()
