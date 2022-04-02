import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []


a = 0.0
for x in range(3):
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    t.goto(x=a, y=t.ycor())
    a -= 20
    segments.append(t)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for x in range(len(segments) - 1, 0, -1):
        newx = segments[x - 1].xcor()
        newy = segments[x - 1].ycor()
        segments[x].goto(x=newx, y=newy)
    segments[0].forward(20)









screen.mainloop()