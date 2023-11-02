import random
import turtle

race_on = False
sc = turtle.Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cord = -70
all_turtles = []

for color in colors:
    ti = turtle.Turtle(shape="turtle")
    ti.up()
    ti.color(color)
    ti.goto(x=-230, y=y_cord)
    y_cord += 30
    all_turtles.append(ti)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        distance = random.randint(0, 10)
        turtle.forward(distance)

sc.exitonclick()
