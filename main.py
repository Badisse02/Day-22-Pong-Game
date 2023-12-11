# split the screen with a discontinued line
# Right Part
# # four squares moving up and down
# # Scoreboard ( each touch of the ball increment the score by one )
# Left Part
# # four squares moving up and down
# # Scoreboard ( each touch of the ball increment the score by one )
# a turtle with shape of square move continuously
# the turtle's headings are 45 / 135 / 225 / 315
# when it goes out it reset in the middle of the screen
from paddle import *
from ball import *
import time
from scoreboard import *
from line import *


s = Screen()
s.setup(800, 600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0)
s.listen()
r_paddle = Paddle(350)
r_paddle.speed("fastest")
s.onkey(key="Up", fun=r_paddle.up)
s.onkey(key="Down", fun=r_paddle.down)

l_s = Scoreboard(-100)
r_s = Scoreboard(100)

dashed_line = Line()
while dashed_line.ycor() < 300 :
    dashed_line.pendown()
    dashed_line.forward(10)
    dashed_line.penup()
    dashed_line.forward(10)

l_paddle = Paddle(-350)
l_paddle.speed("fastest")
s.onkey(key="z", fun=l_paddle.up)
s.onkey(key="s", fun=l_paddle.down)
b = Ball()
s.tracer(1)


l_s.write(b.l_score, align="center", font=("Courier", 80, "normal"))
r_s.write(b.r_score, align="center", font=("Courier", 80, "normal"))

games_is_on = True
speed = 4

while games_is_on:
    b.forward(speed)
    b.change_dir()
    if b.xcor() > 320:
        if b.paddle_touch(r_paddle):
            speed += 1
    elif b.xcor() < -320:
        if b.paddle_touch(l_paddle):
            speed += 1
    if b.ball_out():
        l_s.clear()
        r_s.clear()
        l_s.write(b.l_score, align="center", font=("Courier", 80, "normal"))
        r_s.write(b.r_score, align="center", font=("Courier", 80, "normal"))
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        time.sleep(0.5)
        b.setheading(choice(random_heads))
        speed = 4

s.exitonclick()
