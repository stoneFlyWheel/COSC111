import turtle
import math
turty = turtle.Turtle()

def polyline(n, length, angle):
    for i in range(n):
        turty.forward(length)
        turty.left(angle)

def arc(radius, angle):
    # circumference * fraction of circle
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

def petal(radius, angle):
    arc(radius, angle)
    turty.left(180 - angle)
    arc(radius, angle)
    turty.left(180 - angle)

petal_num = 7
for i in range(0, petal_num):
    petal(100, 360.0 / petal_num)
    turty.left(360.0 / petal_num)
