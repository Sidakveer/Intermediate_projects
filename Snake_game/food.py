import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_rand = random.randint(-280, 280)
        y_rand = random.randint(-280, 280)
        self.goto(x=x_rand, y=y_rand)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=self.xcor() - 20, y=280)
        self.hideturtle()
        self.update(0)

    def update(self, n):
        self.clear()
        self.color("white")
        self.write(f"Score =  {n}",align="center" , font=(f"arial =", 10, "bold"))



