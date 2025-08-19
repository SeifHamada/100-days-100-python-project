from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -280)

    def move_right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - 20, self.ycor())
