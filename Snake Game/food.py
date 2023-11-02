import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.reflresh()

    def reflresh(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.goto(x_cord, y_cord)

