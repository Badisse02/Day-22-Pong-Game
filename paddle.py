from turtle import *


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__("square")
        self.shapesize(1, 5)
        self.penup()
        self.goto(x_pos, 0)
        self.setheading(90)
        self.color("white")


    def up(self):
        if self.ycor() < 240:
            self.forward(30)

    def down(self):
        if self.ycor() > -240:
            self.backward(30)
