"""Draw Squidwards House, looking into the distance."""

__author__ = "730427471"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    spongebob: Turtle = Turtle()
    spongebob.color(0, 0, 0)
    spongebob.speed(50)
    spongebob.screen.bgcolor(176, 243, 248)
    draw_ears(spongebob, 0, 0, 75, 20)
    draw_ceiling(spongebob, -100, 150, 220, 15, 15)
    spongebob.fillcolor(23, 65, 134)
    spongebob.begin_fill()
    draw_shell(spongebob, -120, 130, 500, 260, 280)
    spongebob.end_fill()
    draw_circle(spongebob, -100, 50, 40)
    draw_circle(spongebob, 40, 50, 40)
    spongebob.fillcolor("blue")
    spongebob.begin_fill()
    draw_rectangle(spongebob, -50, 10, 100, 50)
    spongebob.end_fill()
    spongebob.fillcolor(197, 149, 5)
    spongebob.begin_fill()
    draw_rectangle(spongebob, -100, -100, 200, 100)
    spongebob.end_fill()

    done()


def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw a rectangle of the given length and width whose top left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 2:
        a_turtle.forward(width)
        a_turtle.right(90)
        a_turtle.forward(length)
        a_turtle.right(90)
        i += 1 


def draw_ears(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draws two rectangles and fills them in for the ears of Squidward's house."""
    colormode(255)
    a_turtle.pencolor(0, 0, 0)
    a_turtle.fillcolor(23, 65, 134)
    
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, x + 150, y, length, width)
    a_turtle.end_fill()
    
    a_turtle.begin_fill()
    draw_rectangle(a_turtle, x - 150, y, length, width)
    a_turtle.end_fill()


def draw_octagon(a_turtle: Turtle, x: float, y: float, top_length: float, corner_length: float, side_length: float) -> None:
    """Draw an octagon with the specified lengths for each part."""
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.setheading(0.0)

    i: int = 0
    while i < 2:
        a_turtle.forward(top_length)
        a_turtle.right(45)
        a_turtle.forward(corner_length)
        a_turtle.right(45)
        a_turtle.forward(side_length)
        a_turtle.right(45)
        a_turtle.forward(corner_length)
        a_turtle.right(45)
        i += 1


def draw_ceiling(a_turtle: Turtle, x: float, y: float, top_length: float, corner_length: float, side_length: float) -> None:
    """Uses draw_octagon function to draw the ceiling."""
    a_turtle.pencolor(0, 0, 0)
    a_turtle.fillcolor(15, 27, 88)
    a_turtle.begin_fill()
    draw_octagon(a_turtle, x, y, top_length, corner_length, side_length)
    a_turtle.end_fill()


def draw_shell(a_turtle: Turtle, x: float, y: float, length: float, side1_angle: float, side2_angle: float) -> None: 
    """Draws the outline for squidward's house."""
    a_turtle.penup()
    a_turtle.setheading(side1_angle)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.pencolor(0, 0, 0)
    a_turtle.forward(length)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    a_turtle.forward(250)
    a_turtle.penup
    a_turtle.setheading(side2_angle)
    a_turtle.forward(length)
    a_turtle.setheading(180)
    a_turtle.forward(425)


def draw_circle(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a circle."""
    a_turtle.penup()
    a_turtle.color(16, 212, 208)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()


main()