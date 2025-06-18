from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)  

paddle_left = Paddle(-350)
paddle_right = Paddle(350)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_left.move_up, "w")
screen.onkeypress(paddle_left.move_down, "s")
screen.onkeypress(paddle_right.move_up, "Up")
screen.onkeypress(paddle_right.move_down, "Down")

while True:
    time.sleep(0.1)
    screen.update()  
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    if ball.distance(paddle_right) < 30 and ball.xcor() > -340 or ball.distance(paddle_left) < 30 and ball.xcor() > -340:
        ball.collide()
    
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
