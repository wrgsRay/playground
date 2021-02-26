from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = list()

# tim = Turtle(shape='turtle')
# tim.penup()
# tim.goto(-230.0, 0)
turtles_pos = -90.0

for color in colors:
    turtles.append(Turtle(shape='turtle'))
    turtles[-1].penup()
    turtles[-1].color(color)
    turtles[-1].goto(-230.0, turtles_pos)
    turtles_pos += 30.0

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} is the winner!')
            else:
                print(f'You\'ve lost! The {winning_color} is the winner!')
            is_race_on = False
        turtle.forward(randint(0, 10))

screen.exitonclick()
