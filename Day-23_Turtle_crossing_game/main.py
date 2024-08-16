import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

cars = []

# 1. Moving the turtle with keypress
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # 2. Create and move the cars
    car_manager.create_cars()
    car_manager.move_cars()

    # 3. Detecting collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.gameOver()
            game_is_on = False

    if player.check_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increse_level()

screen.exitonclick()
