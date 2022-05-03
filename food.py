from turtle import Turtle
from random import *



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = randint(-450, 450)
        random_y = randint(-320, 320)
        self.goto(random_x, random_y)


