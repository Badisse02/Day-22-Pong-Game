from turtle import *


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(5)
        self.color("White")
        self.goto(0, -280)
        self.setheading(90)

