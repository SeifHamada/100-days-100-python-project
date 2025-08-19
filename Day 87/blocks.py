from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, color="blue"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)


class Bricks:
    def __init__(self):
        self.bricks = []
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    def create_wall(self):
        y_start = 280
        for row in range(5):
            for col in range(-365, 400, 80):
                brick = Brick((col, y_start - row * 30),
                              color=self.colors[row])
                self.bricks.append(brick)

    def check_collision(self, ball):
        for brick in self.bricks:
            if ball.distance(brick) < 30:
                brick.hideturtle()
                self.bricks.remove(brick)
                return True
        return False
