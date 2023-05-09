#Double binary tree
import turtle
import binary_tree as bt

# Proportions
WITDH = 900
HEIGHT = 900

# Setup
turtle.setup(WITDH, HEIGHT)
turtle.seth(90)

# Start
turtle.tracer(0, 0)

# Up tree
for i in range(4):
    turtle.seth(90*i)
    bt.runner(bt.builder(12), 20, 27)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

turtle.penup()
turtle.goto(0, 0)
turtle.seth(90)
turtle.pendown()

# End
turtle.update()
turtle.exitonclick()