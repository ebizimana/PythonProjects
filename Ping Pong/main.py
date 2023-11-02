import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboad

# Initialise classes
screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboad()

# Create the screen
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# Make Paddles move
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Update the screen
game_is_on = True
while game_is_on:
    time.sleep(ball.speed_factor)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.ball_reset()
        score.l_point()
        score.update_scoreboard()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_point()
        score.update_scoreboard()


screen.exitonclick()
