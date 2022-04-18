import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food, Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food1 = Food()
scoreboard1 = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food1) < 15:
        food1.refresh()
        snake.extend()
        scoreboard1.score += 1
        scoreboard1.update(scoreboard1.score)


    #detect collision with the wall
    if snake.head.xcor() > 285 or snake.head.ycor() < -285 or snake.head.xcor() < -285 or snake.head.ycor() > 285:
        scoreboard1.reset_scoreboard()
        snake.reset_snake()

    #detect collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard1.reset_scoreboard()
            snake.reset_snake()


screen.mainloop()