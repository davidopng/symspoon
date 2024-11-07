import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Animated Circle")
screen.bgcolor("white")

# Create a turtle for drawing
circle = turtle.Turtle()
circle.shape("circle")
circle.color("blue")
circle.speed(0)  # Set the drawing speed to the maximum

# Define the initial radius and angle
radius = 50
angle = 1

# Animation loop
while True:
    # Clear the previous drawings
    circle.clear()

    # Update the position of the turtle
    x = radius * (2 ** 0.5) / 2
    y = radius * (2 ** 0.5) / 2
    circle.penup()
    circle.goto(x, y)
    circle.pendown()

    # Draw the circle
    circle.circle(radius)

    # Rotate the circle
    circle.right(angle)

# Keep the window open
turtle.done()
