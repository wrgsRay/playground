from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


snake = list()
for part in range(3):
    snake.append(Turtle(shape='square'))
    snake[part].color('white')
    snake[part].goto(part * -20, 0)














screen.exitonclick()