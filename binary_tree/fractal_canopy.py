import turtle

def reset(x, hd):
    turtle.penup()
    turtle.goto(x)
    turtle.pendown()
    turtle.seth(hd)

def append_2_stack(stack):
    stack.append((turtle.pos(), turtle.heading()))

def segment(stack, stack_2, leng, l_theta, r_theta):
    x, dir = stack.pop(-1)
    reset(x, dir)

    turtle.left(l_theta)
    turtle.fd(leng)
    append_2_stack(stack_2)

    reset(x, dir)

    turtle.right(r_theta)
    turtle.fd(leng)
    append_2_stack(stack_2)

    

# Setup
WIDTH = 900
HEIGHT = 900

turtle.setup(WIDTH, HEIGHT)
turtle.penup()
turtle.goto(0, -HEIGHT/2+50)
turtle.pendown()
turtle.seth(90)


# Code here
turtle.tracer(0, 0)

turtle.seth(90)
n = 5
x = 300
l_theta = 45
r_theta = 45
r = 0.5

# Define stack
stack = []
stack_2 = []

# Trunk
turtle.fd(x)
append_2_stack(stack)
ratio_counter = 1
for _ in range(n):
    ratio = r ** ratio_counter
    if len(stack) == 0:
        stack, stack_2 = stack_2, stack
        ratio_counter = ratio_counter + 1
    for _ in range(len(stack)):
        segment(stack, stack_2, x*ratio, l_theta, r_theta)


turtle.update()

turtle.exitonclick()