from turtle import Screen, Turtle
import turtle as t
from random import choice, randint

tim = Turtle()
t.colormode(255)
tim.pensize(10)
tim.speed(5)


def random_rgb():
    return randint(0, 255), randint(0, 255), randint(0, 255)


for _ in range(100):
    tim.color(random_rgb())
    tim.setheading(choice([0, 90, 180, 270]))
    tim.forward(30)







screen = Screen()
screen.exitonclick()









