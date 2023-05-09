import turtle


def leaf(x):
    x = x / 2
    turtle.fd(x)
    turtle.penup()
    turtle.back(x)
    turtle.pendown()

def branch(x):
    # x = x*(ratio**n)
    turtle.fd(x)


def runner(secuence, x, r):
    # Store in the stack the previous position and direction
    stack = []
    # Repeat for every char in the secuence
    for char in secuence:
        # The outer branches
        if char == "0":
            leaf(x)
        # The inner branches
        elif char == "1":
            branch(x)
        # Append current position and direction and turn left by r
        elif char == "[":
            stack.append((turtle.heading(), turtle.pos()))
            turtle.left(r)
        #Pop the last position and direction and goto them
        elif char == "]":
            # Pop the last position and direction from the stack
            head, pos = stack.pop(-1)
            # Set direction
            turtle.seth(head)
            # Do not draw trayectory to popped position
            turtle.penup()
            turtle.goto(pos)
            turtle.pendown()
            # Turn right by r
            turtle.right(r)

def builder(n):
    # Base secuence
    secuence = "0"
    iteration_buffer = []
    # For amount of iterations (n), for each character in the secuence replace 
    # the character by its rule:
    # "[]" -> Constant, they pass to the buffer as is
    # "1" -> "11"
    # "0" -> 1[0]0
    for _ in range(n):
        for char in secuence:
            if char == "[":
                iteration_buffer.append("[")
            elif char == "]":
                iteration_buffer.append("]")
            elif char == "1":
                iteration_buffer.append("1")
            elif char == "0":
                iteration_buffer.append("1[0]0")
        # Define the secuence as the buffer and empty the buffer for the next iteration
        secuence = "".join(iteration_buffer)
        iteration_buffer = []
    # At the end return the last defined secuence
    return secuence

if __name__ == "__main__":
    screen = turtle.Screen()

    # Proportions
    WITDH = 900
    HEIGHT = 900

    # Setup
    turtle.setup(WITDH, HEIGHT)
    turtle.seth(90)
    turtle.penup()
    # turtle.goto(0, -HEIGHT/2)
    turtle.pendown()

    # Binary tree example
    turtle.tracer(0, 0)

    n = 12
    built_secuence = builder(n)
    print(built_secuence)
    runner(built_secuence, 20, 45)

    turtle.update()

    #Mantain oppened
    turtle.exitonclick()
