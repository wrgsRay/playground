from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", False, align='center', font=('Arial', 20, 'normal'))