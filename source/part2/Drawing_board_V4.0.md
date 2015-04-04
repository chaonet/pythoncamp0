\# CodeSkulptor runs Python programs in your browser.
\# Click the upper left button to run this simple demo.

\# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
\# Some features may work in other browsers, but do not expect
\# full functionality.  It does NOT run in Internet Explorer.
```
import simplegui
```
\# Global Variables
```
WIDTH = 1000
HEIGHT = 600
canvas_color = " "
Polygons = " "
Pol_list = [[WIDTH / 2, HEIGHT / 2, canvas_color, Polygons]]
be = 0
end = 1
review_n = 0
review = False
speed = 500
file_out = []
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
\# Handler for mouse click
```
def click(pos):
    global Pol_list, review, end, review_n, canvas_color, Polygons
    if canvas_color == " ":
        canvas_color = "Red"
    if Polygons == " ":
        Polygons = "Triangular"
    pos_cu = list(pos)
    Pol_list.append([pos_cu[0], pos_cu[1], canvas_color, Polygons])
    end += 1
    review_n = 0
    review = False

def review():
    global review_n, review, file_out
    review = True
    review_n += 1

def start():
    timer.start()
    timer_slow.stop()
    timer_fast.stop()

def stop():
    timer.stop()
    timer_slow.stop()
    timer_fast.stop()

def speed_fast():
    timer_fast.start()
    timer.stop()
    timer_slow.stop()

def speed_slow():
    timer_slow.start()
    timer.stop()
    timer_fast.stop()
```
\# Handler to draw on canvas
```
def draw(canvas) :
    if review == False :
        for Poly in Pol_list[be:end]:
            if Poly[3] == "Triangular":
                canvas.draw_polygon([[Poly[0], Poly[1]-25], [Poly[0]-25, Poly[1]+25], [Poly[0]+25,Poly[1]+25]], 5, "White", Poly[2])
            elif Poly[3] == "Square":
                canvas.draw_polygon([[Poly[0]-25, Poly[1]-25], [Poly[0]-25, Poly[1]+25], [Poly[0]+25, Poly[1]+25], [Poly[0]+25, Poly[1]-25]], 5, "White", Poly[2])
            elif Poly[3] == "Round":
                canvas.draw_circle([Poly[0], Poly[1]], 15, 1, "White", Poly[2])
    else :
        for Poly in Pol_list[be:end-review_n]:
            if Poly[3] == "Triangular":
                canvas.draw_polygon([[Poly[0], Poly[1]-25], [Poly[0]-25, Poly[1]+25], [Poly[0]+25,Poly[1]+25]], 5, "White", Poly[2])
            elif Poly[3] == "Square":
                canvas.draw_polygon([[Poly[0]-25, Poly[1]-25], [Poly[0]-25, Poly[1]+25], [Poly[0]+25, Poly[1]+25], [Poly[0]+25, Poly[1]-25]], 5, "White", Poly[2])
            elif Poly[3] == "Round":
                canvas.draw_circle([Poly[0], Poly[1]], 15, 1, "White", Poly[2])
```
\# Create a frame and assign callbacks to event handlers
```
frame = simplegui.create_frame("Drawing board", 1000, 600)
frame.set_canvas_background('White')

label1 = frame.add_label('shape')
frame.add_button('Triangular', Triangular, 80)
frame.add_button('Square', Square, 80)
frame.add_button('Round', Round, 80)
label2 = frame.add_label('')

label3 = frame.add_label('color')
frame.add_button("Red", red, 60)
frame.add_button("Yellow", yellow, 60)
frame.add_button("Green", green, 60)
frame.add_button("Blue", blue, 60)
frame.add_button("Black", black, 60)

label4 = frame.add_label('')
label5 = frame.add_label('review')
frame.add_button("review_start", start, 100)
label6 = frame.add_label('')
label7 = frame.add_label('speed')
frame.add_button("fast", speed_fast, 100)
frame.add_button("slow", speed_slow, 100)
label6 = frame.add_label('')
frame.add_button("review_stop", stop, 100)

timer = simplegui.create_timer(1000, review)
timer_slow = simplegui.create_timer(2000, review)
timer_fast = simplegui.create_timer(100, review)

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
```
\# Start the frame animation
```
frame.start()
```