from turtle import Turtle
import time


# 4. create the ball and make it move
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_increment = 10
        self.y_increment = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor()+self.x_increment
        new_y = self.ycor()+self.y_increment
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def bounce_y(self):
        self.y_increment *= -1

    def bounce_x(self):
        self.x_increment *= -1
        self.move_speed *= 0.9
