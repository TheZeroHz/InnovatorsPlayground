import turtle
from time import *
# Pre-configured variables for stairs
step_size = 45  # Height and width of each step
movement_history=''
# Initialize screen and turtle objects
screen = turtle.Screen()
screen.title("Kocchop Vaiya")
screen.bgcolor("white")  # Ensure the screen starts blank
# Create an internal turtle object for writing
writer = turtle.Turtle()
# Create the turtle for animation
Kocchop = turtle.Turtle()
Kocchop.shape("turtle")
Kocchop.speed(1)
Kocchop.shapesize(4, 4)
Kocchop.penup()
Kocchop.goto(0, 0)
Kocchop.pendown()

def draw_stairs(steps):
    """Draws the stairs based on the number of steps."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)  # Fastest drawing for stairs
    pen.penup()
    for _ in range(steps):
        pen.pendown()
        pen.forward(step_size)  # Step width
        pen.left(90)
        pen.forward(step_size)  # Step height
        pen.right(90)
    pen.penup()

def show_text(position, value, font=("Arial", 16, "normal")):
    writer.hideturtle()  # Hide the turtle icon
    writer.penup()       # Lift the pen to move without drawing

    # Move to the specified position and write the text
    writer.goto(position)
    writer.clear()  # Clear previous text
    writer.write(value, align="center", font=font)

    # Clean up (optional: keeps the turtle object hidden and stationary)
    writer.penup()

def make_polygon(num_of_sides,size_of_sides):
    for i in range(1000000):
        show_text((0,-110),'Go Forward')
        sleep(1)
        Kocchop.forward(size_of_sides)
        show_text((0, -110), f'turn {360/num_of_sides} degree left')
        sleep(1)
        Kocchop.left(360/num_of_sides)
        sleep(1)