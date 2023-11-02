import turtle
import random

ti = turtle.Turtle()
myScreen = turtle.Screen()
# ti.shape("turtle")
ti.color("coral")

# Setting the screen color-mode
myScreen.colormode(255)


def dash_line():
    for _ in range(50):
        ti.fd(10)
        ti.up()
        ti.fd(10)
        ti.down()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomised_color = (r, g, b)
    return randomised_color


def draw_shapes(shapes, sides):
    while shapes > 0:
        ti.pencolor(random_color())
        for _ in range(sides):
            ti.left(360/sides)
            ti.forward(100)
        sides += 1
        shapes -= 1


# Draw a shapes
total_shapes = 8
minimal_sides = 3
# draw_shapes(total_shapes,sides)


# Draw a Random walk
def draw_random_walk():
    ti.pensize(10)
    random_walk = [0, 90, 180, 270]
    ti.speed("fastest")
    # move up
    for _ in range(500):
        choice = random.choice(random_walk)
        ti.pencolor(random_color())
        ti.setheading(choice)
        ti.forward(50)


# Draw a Spirograph
def draw_spirograph(size_of_gap):
    ti.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        ti.color(random_color())
        ti.circle(100)
        ti.setheading(ti.heading() + size_of_gap)


# draw_spirograph(5)
draw_random_walk()
myScreen.exitonclick()
