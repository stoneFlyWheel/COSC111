import turtle
import math
turty = turtle.Turtle()

# most of the functions were directly copied from the textbook!
# i did not write them myself
# however, i did write petal() and the headache-y stuff at the bottom

# create a function for polyline
def polyline(n, length, angle):
    for i in range(n):
        turty.forward(length)
        turty.left(angle)

# use polyline to create a function for circles & arcs
def arc(radius, angle):
    # circumference * fraction of circle 
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

# use arc to create a function for drawing petals
def petal(radius, angle):
    arc(radius, angle)
    turty.left(180 - angle)
    arc(radius, angle)
    turty.left(180 - angle) # reset where it's going

# the fun part!
petal_num = 7 # adjustable
for i in range(0, petal_num):
    petal(100, 360.0 / petal_num)
    turty.left(360.0 / petal_num)
