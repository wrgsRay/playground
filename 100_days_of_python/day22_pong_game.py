from turtle import Screen, Turtle
from day22_paddle import Paddle
from day22_ball import Ball
from day22_scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Bong Game")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
scoreboard.write_score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
x_direction = 10
y_direction = 10
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move(x_direction, y_direction)
    # Detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        y_direction *= -1

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        x_direction *= -1
        ball.speed()
    if ball.xcor() > 380:
        ball.restart()
        x_direction = -10
        scoreboard.l_score += 1
        ball.move_speed *= 0.5
        scoreboard.write_score()
        ball.move(x_direction, y_direction)
    elif ball.xcor() < -380:
        ball.restart()
        x_direction = 10
        scoreboard.r_score += 1
        ball.move_speed *= 0.5
        scoreboard.write_score()
        ball.move(x_direction, y_direction)
screen.exitonclick()
