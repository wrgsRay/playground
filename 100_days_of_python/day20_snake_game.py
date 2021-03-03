from turtle import Screen
from day20_snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()


while True:
    screen.update()
    time.sleep(0.1)

    snake.move()














screen.exitonclick()