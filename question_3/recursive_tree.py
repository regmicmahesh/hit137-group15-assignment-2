# Program: recursive_tree.py
# Author: Mahesh Chandra Regmi
# Student ID: S383242

import turtle

screen = turtle.Screen()
turtle = turtle.Turtle()

turtle.setheading(90)
turtle.goto(0, 0)



def make_recursive_tree(length, width, depth=1):
    """
    This function makes a recursive tree.
    """

    # This is the base case of the recursion.
    # If the depth is greater than the recursion depth, the function will return.
    if depth > RECURSION_DEPTH:
        return

    # This is the first branch of the tree.
    # If the depth is 1, the color of the tree will be brown.
    # Otherwise, the color of the tree will be green.
    if depth == 1:
        turtle.color("brown")
    else:
        turtle.color("green")

    turtle.width(width)
    turtle.forward(length)

    # We need to save the current heading of the turtle.
    # This is because we need to return to the same heading after drawing the left branch.
    current_heading = turtle.heading()

    turtle.left(LEFT_ANGLE)
    make_recursive_tree(length * REDUCTION_FACTOR, width * REDUCTION_FACTOR, depth + 1)

    # Return to the same heading after drawing the left branch.
    turtle.setheading(current_heading)



    # Repeat the same process for the right branch.
    turtle.right(RIGHT_ANGLE)
    make_recursive_tree(length * REDUCTION_FACTOR, width * REDUCTION_FACTOR, depth + 1)

    turtle.setheading(current_heading)

    turtle.penup()
    turtle.backward(length)
    turtle.pendown()

try:
    LEFT_ANGLE = int(input("Enter the left angle: "))
    RIGHT_ANGLE = int(input("Enter the right angle: "))
    RECURSION_DEPTH = int(input("Enter the recursion depth: "))
    REDUCTION_FACTOR = float(input("Enter the reduction factor: "))
except ValueError:
    print("Invalid input. Please enter valid integers and floats.")
    exit()

make_recursive_tree(100, 3)
screen.exitonclick()
