# Plan

# Create a snake body
# Move the snake
# Control the snake

# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

from turtle import Screen
from sprites import *
import time
from scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#597855")
screen.title('Snake')
screen.tracer()

screen.listen()

snake = Snake()
food = Food()
scoreboard = Board()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

play = True

while play:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        play = False
        snake.hide()
        food.hideturtle()
        scoreboard.game_over()

    # collision with tail
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            play = False
            snake.hide()
            food.hideturtle()
            scoreboard.game_over()

screen.exitonclick()