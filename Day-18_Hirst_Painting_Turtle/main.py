import turtle
import colorgram
from turtle import Turtle, Screen
import random

turtle.colormode(255)

# getting colours from image
# colors = colorgram.extract('image.jpg', 25)

# colour_list = []
# for color in colors:
#     rgb = color.rgb
#     r_g_b_list = (rgb.r, rgb.g, rgb.b)
#     colour_list.append(r_g_b_list)
# print(colour_list)

colour_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

timmy = Turtle()
timmy.hideturtle()
timmy.speed("fastest")

timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()

for i in range(10):
    for j in range(10):
        timmy.dot(20, random.choice(colour_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

    # new line
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
    timmy.pendown()

screen = Screen()
screen.exitonclick()

