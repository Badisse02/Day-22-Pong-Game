from random import *
from paddle import *

random_heads = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(choice(random_heads))
        self.l_score = 0
        self.r_score = 0

    def change_dir(self):
        if (self.ycor() > 280 or self.ycor() < -280) and (self.heading() == 45 or self.heading() == 225):
            self.speed("fastest")
            self.right(90)
            self.speed(3)
        elif (self.ycor() > 280 or self.ycor() < -280) and (self.heading() == 135 or self.heading() == 315):
            self.speed("fastest")
            self.left(90)
            self.speed(3)

    def paddle_touch(self, paddle):
        if self.distance(paddle) < 50:
            if self.heading() == 45 or self.heading() == 225:
                self.speed("fastest")
                self.left(90)
                self.speed(3)
                return True
            else:
                self.speed("fastest")
                self.right(90)
                self.speed(3)
                return True
        return False

    def ball_out(self):
        if self.xcor() > 370:
            self.hideturtle()
            self.goto(0, 0)
            self.showturtle()
            self.forward(0)
            self.l_score += 1
            return True
        elif self.xcor() < -370:
            self.hideturtle()
            self.goto(0, 0)
            self.showturtle()
            self.forward(0)
            self.r_score += 1
            return True
        return False
