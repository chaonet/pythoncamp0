\# CodeSkulptor runs Python programs in your browser.
\# Click the upper left button to run this simple demo.

\# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
\# Some features may work in other browsers, but do not expect
\# full functionality.  It does NOT run in Internet Explorer.
```
import simplegui
import math
```
\# Global Variables
```
WIDTH = 1000
HEIGHT = 600
canvas_color = "Black"
pos = [WIDTH / 2, HEIGHT / 2]
BALL_RADIUS = 15
Polygons = "Round"

def Triangular():
    return
    
def Square():
    return
    
def Round():
    return
```
\# Event Handlers
```
def red():
    global canvas_color
    canvas_color = "Red"

def yellow():
    global canvas_color
    canvas_color = "Yellow"

def green():
    global canvas_color
    canvas_color = "Green"
    
def blue():
    global canvas_color
    canvas_color = "Blue"
    
def black():
    global canvas_color
    canvas_color = "Black"
```
\# Handler for mouse click
```
def click(posin):
    global pos
    pos = list(posin)

def Triangular():
    global Polygons
    Polygons = "Triangular"
    
def Square():
    global Polygons
    Polygons = "Square"
    
def Round():
    global Polygons
    Polygons = "Round"
```
\# Handler to draw on canvas
```
def draw(canvas):
    if Polygons == "Triangular":
        canvas.draw_polygon([(pos[0], pos[1]-25), (pos[0]-25, pos[1]+25), (pos[0]+25,pos[1]+25)], 5, "White", canvas_color)
    elif Polygons == "Square":
        canvas.draw_polygon([(pos[0]-25, pos[1]-25), (pos[0]-25, pos[1]+25), (pos[0]+25, pos[1]+25), (pos[0]+25, pos[1]-25)], 5, "White", canvas_color)
    elif Polygons == "Round":
        canvas.draw_circle(pos, BALL_RADIUS, 1, "White", canvas_color)
```
\# Create a frame and assign callbacks to event handlers
```
frame = simplegui.create_frame("Home", 1000, 600)
frame.set_canvas_background('White')
frame.add_button('Triangular', Triangular, 80)
frame.add_button('Square', Square, 80)
frame.add_button('Round', Round, 80)
frame.add_button("Red", red, 60)
frame.add_button("Yellow", yellow, 60)
frame.add_button("Green", green, 60)
frame.add_button("Blue", blue, 60)
frame.add_button("Black", black, 60)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
```
\# Start the frame animation
```
frame.start()
```