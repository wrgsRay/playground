import turtle as t
from random import choice
# import colorgram
#
# colors = colorgram.extract('day18_image.jpg', 30)
#
# print(colors)
#
# rgb_colors = [tuple(color.rgb) for color in colors]
# print(rgb_colors)

color_list = [(131, 165, 204), (221, 149, 109), (30, 41, 62), (201, 134, 146), (166, 58, 48), (141, 184, 161), (41, 104, 154), (236, 213, 94), (150, 59, 66), (215, 82, 71), (236, 165, 157), (51, 112, 91), (33, 60, 55), (171, 29, 33), (156, 33, 30), (52, 44, 49), (229, 162, 166), (170, 188, 221), (17, 96, 70), (57, 51, 48), (186, 101, 111), (30, 60, 110), (107, 126, 159), (174, 200, 188), (34, 151, 210), (65, 66, 57)]

tim = t.Turtle()
t.colormode(255)
tim.pensize(1)
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
starting_pos = tim.pos()
y_pos = starting_pos[1]
while y_pos <= (starting_pos[1] + 500.0):
    for _ in range(10):
        tim.color(choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    y_pos += 50.0
    tim.goto(starting_pos[0], y_pos)
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()
