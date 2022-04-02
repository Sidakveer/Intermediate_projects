from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
segments = []


a = 0.0
for x in range(3):
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    t.goto(x=a, y=t.ycor())
    a -= 20
    segments.append(t)






screen.mainloop()