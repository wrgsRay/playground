from turtle import Screen, Turtle
from random import randint, random

tim = Turtle()


sides = 3
while sides < 11:
    tim.color(random(), random(), random())
    for _ in range(sides):
        tim.forward(100)
        tim.right(360/sides)
    sides += 1






screen = Screen()
screen.exitonclick()









