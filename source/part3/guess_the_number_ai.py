import pygame
import random

pygame.init()

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
    done = False
    clock = pygame.time.Clock()
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is 10","\n"
    num_random = random.randint(0, 100)
    print num_random
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
      print "Number of remaining guess is",num_try

      if guess > num_random:
         print "Higher","\n"
         status = "Higher"
      elif guess < num_random:
         print "Lower","\n"
         status = "Lower"
      else :
         print "Correct!","\n"
         #new_game()
         done=True
         exit()


# create frame

screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("Guess number")

pygame.draw.rect(screen, [0,0,0], [150, 10, 50, 20], width=0)

screen.fill(WHITE)

pygame.display.flip()


pygame.quit()

# register event handlers for control elements and start frame


# call new_game 

new_game()
