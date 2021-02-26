from turtle import Screen, Turtle
import turtle as t
from random import choice, randint

tim = Turtle()
t.colormode(255)
tim.pensize(1)
tim.speed(0)


def random_rgb():
    return randint(0, 255), randint(0, 255), randint(0, 255)


tilt_degree = 10
for _ in range(int(360/tilt_degree)):
    tim.color(random_rgb())
    tim.circle(100)
    tim.right(tilt_degree)







screen = Screen()
screen.exitonclick()









