from turtle import Turtle
from random import *


class Food:
    def __init__(self):
        self.p_food = Turtle(shape="circle")
        self.p_food.color("red")
        self.p_food.turtlesize(stretch_len=1, stretch_wid=1)
        self.p_food.penup()
        self.refresh_food()

    def refresh_food(self):
        random_x = randint(-450, 450)
        random_y = randint(-320, 320)
        self.p_food.goto(random_x, random_y)
