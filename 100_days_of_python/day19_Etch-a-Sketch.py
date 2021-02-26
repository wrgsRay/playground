from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_ccw():
    tim.left(5)


def turn_cw():
    tim.right(5)


def clear():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_ccw, 'a')
screen.onkey(turn_cw, 'd')
screen.onkey(clear, 'c')

screen.exitonclick()
