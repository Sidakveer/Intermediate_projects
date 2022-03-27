import random
import turtle
from turtle import *

angles = (0, 90, 180, 270)
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
current_heading = tim.heading()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

for i in range(75):
    tim.circle(100)
    colour = tim.color(random_color())
    current_heading += 5
    tim.setheading(current_heading)


screen = Screen()
screen.exitonclick()


