from turtle import Turtle
from random import *
score = 0


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        with open("/Users/ELCOT/Documents/high score data.txt") as data:
            self.high_score1 = int(data.read())
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.goto(-50, 300)
        self.clear()
        self.write(f"score = {self.score}    High score = {self.high_score1}", align="center", font=("Arial", 15, "normal"), )

    def increase_score(self):
        self.score += 1
        self.display_score()

    def high_score(self):
        if self.score > self.high_score1:
            self.goto(-20, 0)
            self.write("NEW HIGH SCORE")
            self.high_score1 = self.score
            self.refresh()
            with open("/Users/ELCOT/Documents/high score data.txt", mode="w") as data:
                data.write(f"{self.high_score1}")

        self.display_score()

    def refresh(self):
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 15, "normal"), )

