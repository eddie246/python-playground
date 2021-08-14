from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.penup()
    # self.shapesize(0.5, 0.5)
    self.color('red')
    self.speed('fastest')
    self.move_food()

  def move_food(self):
    coords = [-14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    self.goto(random.choice(coords) * 20, random.choice(coords) * 20)