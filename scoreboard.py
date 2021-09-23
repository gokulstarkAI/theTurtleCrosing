from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALINE = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"level: {self.level}", align=ALINE, font=FONT)

    def level_increase(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALINE, font=FONT)
        self.goto(-200, 250)
        self.write(f"level: {self.level}", align=ALINE, font=FONT)
