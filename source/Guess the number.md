\# template for "Guess the number" mini-project

\# input will come from buttons and an input field

\# all output for the game will be printed in the console

```
import simplegui

import math

import random

num_range = 100
```
\# helper function to start and restart the game

```
def new_game():
    # initialize global variables used in your code here
    global num_random, n
    n = 0
    print "New game. Range is from 0 to ", num_range
    print "Number of remaining guesses is", (math.log(num_range, 10)*3 +1),"\n"
    num_random = random.randrange(0, num_range)
    input_guess
    pass
```

\# define event handlers for control panel

```
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    pass
    
  
def input_guess(guess):
    # main game logic goes here	
    global num_random , n
    n += 1.0
    print "Guess was",int(guess)
    num_try= (math.log(num_range, 10)* 3+ 1) - n
    print "Number of remaining guess is",num_try
    if int(guess) > num_random:
        print "Higher!","\n"
    elif int(guess) < num_random:
        print "Lower!","\n"
    elif int(guess) == num_random:
        print "Correct!","\n"
        new_game()
    pass
```

\# create frame

```
f = simplegui.create_frame("Guess the number",200,200)
```
\# register event handlers for control elements and start frame

```
f.add_button("Range is [0,100)", range100, 100)
f.add_button("Range is [0,1000)", range1000, 100)
f.add_input("Enter a guess", input_guess, 100)
```
\# call new_game 

```
new_game()
```

\# always remember to check your completed program against the grading rubric
