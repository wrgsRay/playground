from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


snake = list()
x_pos = 0
for part in range(3):
    snake.append(Turtle(shape='square'))
    snake[part].color('white')
    snake[part].goto(x_pos * -1, 0)
    x_pos += 20














screen.exitonclick()