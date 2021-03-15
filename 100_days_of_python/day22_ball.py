from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.color('white')
        self.move_speed = 0.1

    def move(self, x_direction, y_direction):
        self.goto(self.xcor() + x_direction, self.ycor() + y_direction)

    def restart(self):
        self.goto(0, 0)
        self.move_speed = 0.1

