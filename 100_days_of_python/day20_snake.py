from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = list()
        self.create_snake()

    def create_snake(self):
        for segment in range(3):
            self.segments.append(Turtle(shape='square'))
            self.segments[segment].color('white')
            self.segments[segment].penup()
            self.segments[segment].goto(segment * -20, 0)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
