from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.ht()
        self.goto(-200, 250)
        self.lever = 1
        self.write_level()

    def increase_level(self):
        self.lever += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"Lever: {self.lever} ", align="center", font=FONT)

    def game_is_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write("Game is over", align="center", font=FONT)
