from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create the snake, food, scoreboard
snake = Snake()
food = Food()
keep_score = Score()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.reflresh()
        snake.extend()
        keep_score.increase()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        keep_score.reset()
        snake.reset()

    # Detect collision with tail
    for seg in snake.segments[3:]:
        if snake.head.distance(seg) < 10:
            keep_score.reset()
            snake.reset()


# Exit the game
screen.exitonclick()
