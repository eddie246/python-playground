from turtle import Turtle
import random

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.speed('fastest')
    self.color('white')
    self.shape('circle')
    self.setheading(135)
    # self.setheading(180)
    self.move_ball()
  
  def move_ball(self):
      self.forward(5)
  
  def bounce(self):
    # self.left(random.randint(85, 95))
    self.left(90)

  def reset(self):
    self.home()
    self.setheading(135)
