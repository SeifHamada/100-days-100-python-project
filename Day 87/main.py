from turtle import Turtle, Screen
from ball import Ball
import time
from paddle import Paddle
from blocks import Bricks

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Breakout Game")
screen.tracer(0)

ball = Ball()
paddle = Paddle()
bricks = Bricks()
bricks.create_wall()

screen.listen()
screen.onkeypress(paddle.move_left, "a")
screen.onkeypress(paddle.move_right, "d")


def show_message(message):
    msg = Turtle()
    msg.hideturtle()
    msg.color("white")
    msg.penup()
    msg.goto(0, 0)
    msg.write(message, align="center", font=("Courier", 32, "bold"))


while True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() < -260 and abs(ball.xcor() - paddle.xcor()) < 50:
        ball.collide()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce()

    if ball.ycor() > 280:
        ball.collide()

    if ball.ycor() < -300:
        show_message("GAME OVER")

    if bricks.check_collision(ball):
        ball.collide()

    if not bricks.bricks:
        show_message("YOU WIN!")
