import turtle
import math as m
screen = turtle.Screen()

#setup
turtle.setup(900,900)
turtle.left(90)

def leaf(x):
    turtle.fd(x)
    turtle.backward(x)

def branch(x):
    turtle.fd(x)

def push(x):
    turtle.left(45)
    branch(x)

def pop(x):
    turtle.right(45)
    branch(x)

def builder(path):
    for char in path:
        if char == "0":
            path = path.replace("0", "1[0]0")
        if char == "1":
            path = path.replace('1', '11')
    return path

def runner(path, x):
    for char in path:
        if char == "0":
            leaf(x)
        elif char == "1":
            branch(x)
        elif char == "[":
            push(x)
        elif char == "]":
            pop(x)
        

#Binary tree
n = 1
secuence = "0"
secuence = builder(secuence)

runner(secuence, 100)





    
    

turtle.exitonclick()


