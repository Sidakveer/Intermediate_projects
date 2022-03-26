import random
from turtle import *

tim = Turtle()

tim.color("red")
tim.penup()
tim.forward(100)
tim.pendown()


for i in range(3, 11):
    angle = 360 / i
    colour = tim.color(random.choice(["red", "green", "blue", "yellow"]))
    for x in range(i):
        tim.right(angle)
        tim.forward(100)

screen = Screen()
screen.exitonclick()

