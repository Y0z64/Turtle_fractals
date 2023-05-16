import turtle

class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        pass
    
    def __len__(self) -> int:
        return self.stack1.__len__()

    def append_2_stack(self, foo) -> None:
        self.stack2.append(foo)

    def pop_stack(self) -> tuple[tuple[float, float], float]:
        position, direction = self.stack1.pop(-1)
        return (position, direction)

    def reverse_stacks(self) -> None:
        self.stack1, self.stack2 = self.stack2, self.stack1

class Fractal:
    def __init__(self, height:int, width: int, home: bool = False, ini_dir: float = 90, offset: float = 0) -> None:
        self.HEIGHT = height
        self.WIDTH = width

        self.turtle = turtle.Turtle()
        self.stack: Stack = Stack()
        self.turtle.seth(ini_dir)

        if home:
            self.silent_goto((0, (-self.HEIGHT/2)+offset), ini_dir)
    
    def display_trunk(self, length: float,  trunk: bool = True):
        if trunk:
            self.turtle.fd(length)
        else:
            self.turtle.penup()
            self.turtle.fd(length)
            self.turtle.pendown()

    def get_vector(self) -> tuple[tuple[float, float], float]:
        position = self.turtle.pos() 
        direction = self.turtle.heading()
        return (position, direction)

    
    def silent_goto(self, pos: tuple[float, float], dir: float) -> None:
        self.turtle.penup()
        self.turtle.goto(pos)
        self.turtle.pendown()
        self.turtle.setheading(dir)

    def segment(self, l_leng: float,  r_leng: float, l_theta: float, r_theta: float) -> None:
        position, direction = self.stack.pop_stack()
        self.silent_goto(position, direction)

        self.turtle.left(l_theta)
        self.turtle.fd(l_leng)
        self.stack.append_2_stack(self.get_vector())

        self.silent_goto(position, direction)

        self.turtle.right(r_theta)
        self.turtle.fd(r_leng)
        self.stack.append_2_stack(self.get_vector())

    def generate_fractal(self, n: int, seg_length: float, left_ratio: float, right_ratio: float, left_theta: float, right_theta: float,  trunk: bool = True) -> None:
        self.display_trunk(seg_length, trunk)
        self.stack.append_2_stack(self.get_vector())

        l_x, r_x = seg_length, seg_length
        for _ in range(n):
            if len(self.stack) == 0:
                self.stack.reverse_stacks()
                l_x = l_x * left_ratio
                r_x = r_x * right_ratio
            for _ in range(len(self.stack)):
                self.segment(l_x*left_ratio, r_x*right_ratio, left_theta, right_theta)

if __name__ == "__main__":
    #Setup
    HEIGHT = 900
    WIDTH = 900

    #Parameters
    n = 13
    x = 300
    l_r = 0.7
    r_r = 0.7
    l_theta = 20
    r_theta = 90

    turtle.tracer(0 ,0)
    myFractal = Fractal(HEIGHT, WIDTH, True, offset=100)
    myFractal.generate_fractal(n, x, l_r, r_r, l_theta, r_theta, True)
    turtle.update()
    turtle.exitonclick()






