"""Turtle Movement"""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.color("green")
bob.color("black")

leo.penup()
bob.penup()
leo.goto(-130, 130)
bob.goto(-130, 130)
leo.pendown()
bob.pendown()

side_length: int = 300

leo.speed(50)
bob.speed(75)

i: int = 0

leo.begin_fill()
while i < 3:
    leo.forward(side_length)
    leo.right(120)
    i += 1 
leo.hideturtle()

i: int = 0

while i < 3:
    bob.forward(side_length)
    bob.right(120)
    i += 1

i: int = 0

while i < 200:
    bob.forward(side_length)
    bob.right(125)
    side_length = side_length * 0.97
    i += 1

done()
