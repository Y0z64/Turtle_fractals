import turtle

class FractalTree:
    def __init__(self, screen=None):
        # Initialize the turtle and screen if not provided
        if screen:
            self.screen = screen
        else:
            self.screen = turtle.Screen()
        
        self.t = turtle.Turtle()
        self.t.speed(0)  # Fastest speed
        self.stack = []  # Stack for storing positions and directions
    
    def leaf(self, x):
        """Draw a leaf structure of size x"""
        x = x / 2
        self.t.fd(x)
        self.t.penup()
        self.t.back(x)
        self.t.pendown()
    
    def branch(self, x):
        """Draw a branch of size x"""
        self.t.fd(x)
    
    def runner(self, sequence, x, r):
        """
        Execute the L-system sequence
        
        Args:
            sequence: The L-system string to interpret
            x: Size of the branches
            r: Rotation angle in degrees
        """
        # Start heading upright
        self.t.left(90)
        
        # Clear the stack at the beginning
        self.stack = []
        
        # Repeat for every char in the sequence
        for char in sequence:
            # The outer branches
            if char == "0":
                self.leaf(x)
            # The inner branches
            elif char == "1":
                self.branch(x)
            # Append current position and direction and turn left by r
            elif char == "[":
                self.stack.append((self.t.heading(), self.t.pos()))
                self.t.left(r)
            # Pop the last position and direction and goto them
            elif char == "]":
                # Pop the last position and direction from the stack
                head, pos = self.stack.pop(-1)
                # Set direction
                self.t.seth(head)
                # Do not draw trajectory to popped position
                self.t.penup()
                self.t.goto(pos)
                self.t.pendown()
                # Turn right by r
                self.t.right(r)
        
        self.exit()
    
    def builder(self, n):
        """
        Build the L-system sequence for n iterations
        
        Args:
            n: Number of iterations
            
        Returns:
            The generated L-system string
        """
        # Base sequence
        sequence = "0"
        iteration_buffer = []
        
        # For amount of iterations (n), for each character in the sequence replace 
        # the character by its rule:
        # "[]" -> Constant, they pass to the buffer as is
        # "1" -> "11"
        # "0" -> 1[0]0
        for _ in range(n):
            for char in sequence:
                if char == "[":
                    iteration_buffer.append("[")
                elif char == "]":
                    iteration_buffer.append("]")
                elif char == "1":
                    iteration_buffer.append("1")
                elif char == "0":
                    iteration_buffer.append("1[0]0")
            
            # Define the sequence as the buffer and empty the buffer for the next iteration
            sequence = "".join(iteration_buffer)
            iteration_buffer = []
        
        # At the end return the last defined sequence
        return sequence
    
    def draw_tree(self, iterations, x, r, print=False):
        """
        Main method to draw the fractal tree
        
        Args:
            iterations: Number of iterations for the L-system
            x: Length of the branches
            r: Angle of rotation in degrees
        """
        # Reset position
        self.t.home()
        
        # Build the L-system sequence
        sequence = self.builder(iterations)
        if print:
            print(sequence)
        
        # Execute the sequence
        self.runner(sequence, x, r)
        
        self.exit()
    
    def setup(self, title="Fractal Tree", width=900, height=900, background_color="white", skip=False):
        """Configure the screen settings"""
        self.screen.title(title)
        self.screen.setup(width, height)
        self.screen.bgcolor(background_color)
        

        if skip:
            self.screen.tracer(0)
            self.t.speed(0) # Set speed to maximum to not have to wait for the turtle to finish drawing


    def exit(self):
        # Reset turtle
        self.t.penup()
        self.t.home()
        self.screen.exitonclick()


# Example usage:
if __name__ == "__main__":
    # Create an instance of the FractalTree class
    tree = FractalTree()
    
    # Setup the screen
    tree.setup(title="Fractal Tree L-System")
    
    # Draw a tree with 4 iterations, branch length of 20, and angle of 25 degrees
    tree.draw_tree(iterations=4, x=20, r=25)