# Double binary tree
import turtle
from fractal_tree import FractalTree

def hidden_fd(x):
    turtle.penup()
    turtle.fd(x)
    turtle.pendown()

# Create an instance of FractalTree
tree = FractalTree()
tree.setup()


def regular_tree():
    # Up tree
    n = 5
    sequence = tree.builder(n)
    print(sequence)
    tree.runner(sequence, 30, 27)


# End

# The commented examples can be uncommented and modified to use the FractalTree class like this:

# # Chaotic results
# # # Up tree
# # for i in range(4):
# #     angle = 90
# #     tree.t.seth(angle*i)
# #     tree.runner(tree.builder(10), 20, 27)
# #     tree.t.fd(250)
# #     tree.runner(tree.builder(8), 15, 27)
# #     tree.t.penup()
# #     tree.t.goto(0, 0)
# #     tree.t.pendown()
# #     tree.t.fd(350)
# #     tree.runner(tree.builder(7), 11, 27)

# # Deep field
# # for i in range(4):
# #     angle = 90
# #     fractal_angle = 27
# #     tree.t.seth(angle*i)
# #     tree.runner(tree.builder(10), 20, 27)
# #     tree.t.fd(250)
# #     tree.runner(tree.builder(9), 17, 27)
# #     tree.go_home()
# #     tree.t.fd(300)
# #     direction = tree.t.heading()
# #     tree.runner(tree.builder(10), 50, 60)
# #     tree.go_home()
# #     tree.t.seth(direction)
# #     tree.t.fd(300)
# #     tree.t.right(10)
# #     tree.runner(tree.builder(10), 50, 60)
# #     tree.go_home()
# #     tree.t.seth(direction)
# #     tree.t.fd(300)
# #     tree.t.left(10)
# #     tree.runner(tree.builder(10), 50, 60)
# #     tree.go_home()

if __name__ == "__main__":
    regular_tree()