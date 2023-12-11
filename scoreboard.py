from turtle import *


class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x, 200)


