import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ").lower()
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# it will store all the instance created from Turtle class
turtles = []

i = 0
for _ in colours:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(_)
    new_turtle.penup()
    new_turtle.goto(-230, -70 + i)
    i += 30
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

winner = ""

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 240:
            winner = turtle.pencolor()
            is_race_on = False
            break

if winner == user_bet:
    print("You win the bet.")
else:
    print(f"You lose. {winner} wins the race.")

screen.exitonclick()
