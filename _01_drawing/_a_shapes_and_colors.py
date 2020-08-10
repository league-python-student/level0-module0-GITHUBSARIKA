import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    myTurtle = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    turtle.shape("turtle")
    # Set your turtle's speed using .speed(2)
    turtle.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    turtle.color("cornflower blue")
    turtle.pencolor("plum")
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    #turtle.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    #turtle.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
            turtle.forward(100)
            turtle.right(90)

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    turtle.goto(50, 75)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    turtle.begin_fill()
    turtle.circle(100, steps=30)
    turtle.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    for i in range(3):
        turtle.forward(90)
        turtle.right(360/3)
    for i in range(5):
        turtle.forward(90)
        turtle.right(360/5)
    for i in range(6):
        turtle.forward(90)
        turtle.right(360/6)
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
