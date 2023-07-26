from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.direction = direction
        self.create(self.direction)

    def create(self, direction):
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")

        if direction == "left":
            self.goto(-260, 0)

        if direction == "right":
            self.goto(260, 0)

    def up(self):
        if self.ycor() < 220:
            new_y = self.ycor() + 20
            x = self.xcor()
            self.goto(x, new_y)

    def down(self):
        if self.ycor() > -220:
            new_y = self.ycor() - 20
            x = self.xcor()
            self.goto(x, new_y)
