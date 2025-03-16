import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("purple")
        self.speed("normal")
        self.penup()
        self.refresh()

    def refresh(self):
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-190, 190)
        self.goto(x_pos, y_pos)
