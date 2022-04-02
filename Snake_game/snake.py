from turtle import Turtle

move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        a = 0.0
        for x in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(x=a, y=t.ycor())
            a -= 20
            self.segments.append(t)

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[x - 1].xcor()
            newy = self.segments[x - 1].ycor()
            self.segments[x].goto(x=newx, y=newy)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)