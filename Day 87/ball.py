from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(self.xcor() - self.x, self.ycor() - self.y)

    def collide(self):
        self.y *= -1

    def bounce(self):
        self.x *= -1
