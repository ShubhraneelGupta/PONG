from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


SPEED = 0.1


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("PONG")


left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
sb = Scoreboard()


screen.listen()
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED)
    ball.move()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -235 or ball.distance(right_paddle) < 50 and ball.xcor() > 235:
        ball.x_bounce()
    if ball.xcor() > 280:
        ball.goto(0, 0)
        sb.score1 += 1
    if ball.xcor() < -280:
        ball.goto(0, 0)
        sb.score2 += 1
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    sb.update()


screen.exitonclick()
