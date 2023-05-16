import turtle

def reset(x, hd):
    turtle.penup()
    turtle.goto(x)
    turtle.pendown()
    turtle.seth(hd)

def append_2_stack(stack):
    stack.append((turtle.pos(), turtle.heading()))

def triple_segment(stack, stack_2, l_leng, r_leng, l_theta, r_theta):
    x, dir = stack.pop(-1)
    reset(x, dir)

    turtle.pd(l_leng)
    append_2_stack(stack_2)

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
