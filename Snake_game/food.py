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
        self.score = 0
        self.high_score = 0
        self.goto(x=self.xcor() - 20, y=280)
        self.hideturtle()
        self.update(0)

    def reset_scoreboard(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.update(self.score)

    # def game_over(self):
    #     self.color("white")
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align="center" , font=(f"arial =", 24, "bold"))

    def update(self, n):
        self.clear()
        self.color("white")
        self.write(f"Score =  {n}  High Score: {self.high_score}",align="center", font=(f"arial =", 18, "bold"))


