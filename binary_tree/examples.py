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

def hidden_fd(x):
    turtle.penup()
    turtle.fd(x)
    turtle.pendown()

# Up tree
for i in range(4):
    angle = 90
    fractal_angle = 27
    turtle.seth(angle*i)
    bt.runner(bt.builder(10), 20, 27)
    hidden_fd(250)
    bt.runner(bt.builder(9), 17, 27)
    bt.go_home()
    hidden_fd(300)
    direction = turtle.heading()
    bt.runner(bt.builder(10), 50, 60)
    bt.go_home()
    turtle.seth(direction)
    hidden_fd(300)
    turtle.right(10)
    bt.runner(bt.builder(10), 50, 60)
    bt.go_home()
    turtle.seth(direction)
    hidden_fd(300)
    turtle.left(10)
    bt.runner(bt.builder(10), 50, 60)
    bt.go_home()


#Reset turtle
bt.go_home()
turtle.seth(90)

# End
turtle.update()
turtle.exitonclick()

# Caotic results 
# # Up tree
# for i in range(4):
#     angle = 90
#     turtle.seth(angle*i)
#     bt.runner(bt.builder(10), 20, 27)
#     turtle.fd(250)
#     bt.runner(bt.builder(8), 15, 27)
#     turtle.penup()
#     turtle.goto(0, 0)
#     turtle.pendown()
#     turtle.fd(350)
#     bt.runner(bt.builder(7), 11, 27)

# Deep field
# for i in range(4):
#     angle = 90
#     fractal_angle = 27
#     turtle.seth(angle*i)
#     bt.runner(bt.builder(10), 20, 27)
#     turtle.fd(250)
#     bt.runner(bt.builder(9), 17, 27)
#     bt.go_home()
#     turtle.fd(300)
#     direction = turtle.heading()
#     bt.runner(bt.builder(10), 50, 60)
#     bt.go_home()
#     turtle.seth(direction)
#     turtle.fd(300)
#     turtle.right(10)
#     bt.runner(bt.builder(10), 50, 60)
#     bt.go_home()
#     turtle.seth(direction)
#     turtle.fd(300)
#     turtle.left(10)
#     bt.runner(bt.builder(10), 50, 60)
#     bt.go_home()