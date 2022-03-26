import random
from turtle import *

angles = (0, 90, 180, 270)

tim = Turtle()
tim.speed(100)
tim.hideturtle()
tim.pensize(10)

for i in range(100):
    tim.setheading(random.choice(angles))
    tim.forward(10)
    colour = tim.color(random.choice(["red", "green", "blue", "yellow"]))



screen = Screen()
screen.exitonclick()