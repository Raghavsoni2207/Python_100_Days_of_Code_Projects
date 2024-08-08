from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        # 1. Create snake body
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        # increase body of snake
        self.add_body(self.turtles[-1].position())



    def move(self):
        # 2. Move snake body
        for i in range(len(self.turtles) - 1, 0, -1):
            x_coordinate = self.turtles[i - 1].xcor()
            y_coordinate = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x_coordinate, y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # 3. Controlling snake body
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # 3. Controlling snake body
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # 3. Controlling snake body
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # 3. Controlling snake body
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
