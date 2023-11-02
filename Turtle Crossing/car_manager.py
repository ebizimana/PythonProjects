import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.generate_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            random_y = random.randint(-250, 250)
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.turtlesize(stretch_wid=1, stretch_len=2)
            car.up()
            car.goto(280, random_y)
            self.cars_list.append(car)

    def move_car(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
