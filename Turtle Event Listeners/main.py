import turtle

"""
W = Forwards
S = Backwards
A = Counter-Clockwise
D = Clockwise
C = Clear Drawing
"""

ti = turtle.Turtle()
sc = turtle.Screen()
sc.listen()


# Move Forward
def turtle_forward():
    ti.setheading(0)
    ti.forward(10)
sc.onkey(turtle_forward, "w")

# Move Backward
def turtle_backward():
    ti.backward(10)
sc.onkey(turtle_backward, "s")

# Move Counter-Clockwise
def turtle_left():
    ti.setheading(ti.heading() + 10)
    ti.forward(10)
sc.onkey(turtle_left, "a")

# Move Clockwise:
def turtle_right():
    ti.setheading(ti.heading() - 10)
    ti.forward(10)
sc.onkey(turtle_right, "d")

# Clear drawing
def turtle_clear():
    ti.clear()
    ti.up()
    ti.home()
    ti.down()
sc.onkey(turtle_clear, "c")

sc.exitonclick()

