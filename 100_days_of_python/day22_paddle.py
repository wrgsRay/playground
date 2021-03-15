from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_ycor):
        super().__init__()
        self.starting_ycor = starting_ycor
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.pu()
        self.goto(self.starting_ycor, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
