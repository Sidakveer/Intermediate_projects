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
player_score = 0
while game_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food1) < 15:
        food1.refresh()
        player_score += 1
        scoreboard1.update(player_score)








screen.mainloop()