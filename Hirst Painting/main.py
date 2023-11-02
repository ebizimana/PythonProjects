import random
import turtle

color_list = [(207, 157, 113), (222, 232, 224), (126, 174, 194), (133, 181, 154), (33, 116, 152), (204, 136, 151),
              (228, 202, 119), (237, 220, 223), (204, 218, 225), (141, 85, 58), (157, 61, 80), (207, 77, 95),
              (44, 129, 89), (221, 81, 61), (233, 164, 175), (67, 161, 117), (176, 153, 56), (231, 172, 162),
              (165, 206, 186), (40, 160, 188), (160, 28, 45), (14, 47, 75), (16, 95, 64), (73, 39, 29),
              (161, 204, 214), (148, 33, 26), (19, 66, 47), (72, 32, 46), (6, 93, 109)]

"""
1. Create a 10 by 10 pattern
2. Paint 100 dots using the color palette 
3. Each of your dots should be around 20 in size
4. Each of your dots should be apart by around 50 paces
"""

ti = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

ti.up()
ti.setx(-200)
ti.sety(-200)
ti.speed("fastest")
ti.hideturtle()
current_x = round(ti.xcor(), 2)

rows = 0
while rows < 10:
    current_y = round(ti.ycor(), 2)
    for _ in range(10):
        color = random.choice(color_list)
        ti.dot(20, color)
        ti.up()
        ti.forward(50)
    ti.setx(current_x)
    ti.sety(current_y + 50)
    rows += 1

screen.exitonclick()
