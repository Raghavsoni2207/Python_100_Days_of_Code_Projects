from turtle import Turtle
FONT = ("Courier", 24, "normal")


# 5. Create a scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.update_screen()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)

    def update_screen(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increse_level(self):
        self.level += 1
        self.update_screen()
