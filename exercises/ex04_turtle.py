"""Draw Squidward's House."""

__author__ = "730427471"

from turtle import Turtle, colormode, done
import turtle 
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    spongebob: Turtle = Turtle()
    draw_rectangle(spongebob, 100, 100, 100, 200)
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    done()


def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draws rectangle with given length and width with top left corner at x,y"""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(length)
    a_turtle.right(90)
    a_turtle.forward(width)
    a_turtle.right(90)
    a_turtle.forward(length)
    
# TODO: Use the __name__ is "__main__" idiom shown in 