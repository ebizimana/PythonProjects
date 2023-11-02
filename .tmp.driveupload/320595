import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialise the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# initialise the classes
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Move player
screen.onkey(player.move_up, "Up")

# Game starts
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a car
    cars.generate_car()
    cars.move_car()

    # level finished
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        cars.level_up()

    # Detect player collide with car
    for car in cars.cars_list:
        if car.distance(player) < 27:
            scoreboard.game_is_over()
            game_is_on = False

screen.exitonclick()
