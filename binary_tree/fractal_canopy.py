import turtle

screen = turtle.Screen()

WITDH = 900
HEIGHT = 900
# Setup
turtle.setup(WITDH, HEIGHT)
turtle.seth(90)
turtle.penup()
turtle.goto(0, -HEIGHT/2)
turtle.pendown()

def branch(x, r):
    turtle.fd(x*r)



turtle.tracer(0, 0)
# Code goes here
stack = []
n = 3
for i in range(n):
    x = 200
    r = (5/8)

    r = r**len(stack)
    branch(x, r)
    stack.append(turtle.pos())
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()


turtle.update()


turtle.exitonclick()