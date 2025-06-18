import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    if player.ycor() > 280:
        player.reset_position()
        car.increase_speed()
        scoreboard.increase_score()

    for c in car.all_cars:
        if player.distance(c) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()