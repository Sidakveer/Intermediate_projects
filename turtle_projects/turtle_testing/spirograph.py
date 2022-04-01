import random
import turtle
from turtle import *

angles = (0, 90, 180, 270)
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    for i in range(360 // size_of_gap):
        tim.circle(100)
        colour = tim.color(random_color())
        # size_of_gap += 5
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()
