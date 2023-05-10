import turtle

def reset(x, hd):
    turtle.penup()
    turtle.goto(x)
    turtle.pendown()
    turtle.seth(hd)

def append_2_stack(stack):
    stack.append((turtle.pos(), turtle.heading()))

def segment(stack, stack_2, l_leng, r_leng, l_theta, r_theta):
    x, dir = stack.pop(-1)
    reset(x, dir)

    turtle.left(l_theta)
    turtle.fd(l_leng)
    append_2_stack(stack_2)

    reset(x, dir)

    turtle.right(r_theta)
    turtle.fd(r_leng)
    append_2_stack(stack_2)

    

# Setup
WIDTH = 900
HEIGHT = 900

turtle.setup(WIDTH, HEIGHT)
turtle.penup()
turtle.goto(0, -HEIGHT/2+200)
turtle.pendown()
turtle.seth(90)


# Code here
turtle.tracer(0, 0)

turtle.seth(90)
n = 13
x = 250
l_theta = 45
r_theta = 120
l_r = 0.75
r_r = 0.6

# Define stack
stack = []
second_stack = []

# Trunk
turtle.penup()
turtle.fd(x)
turtle.pendown()
append_2_stack(stack)
l_x, r_x = x, x
for _ in range(n):
    if len(stack) == 0:
        stack, second_stack = second_stack, stack
        l_x = l_x * l_r # Try modifying this so it does not multiply l_x but x
        r_x = r_x * r_r # same here
    for _ in range(len(stack)):
        segment(stack, second_stack, l_x*l_r, r_x*r_r, l_theta, r_theta)


turtle.update()

turtle.exitonclick()