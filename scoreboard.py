from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.create()

    def create(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.write(f"{self.score1} | {self.score2}", align="center", font=("ariel", 30, "bold"))

    def update(self):
        self.clear()
        self.create()
