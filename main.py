import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)

player_1 = Player()
cars = CarManager()
scoreboard = Scoreboard()

scoreboard.update_level()
screen.listen()
screen.onkey(player_1.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    # player reaches the other end
    if player_1.ycor() > 280:
        player_1.reached_edge()
        scoreboard.level_increase()
        cars.level_up_cars()

    # detect collision with cars
    for car in cars.all_cars:
        if car.distance(player_1) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()
