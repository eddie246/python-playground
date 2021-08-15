from turtle import Turtle

class Paddle(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.speed('fastest')
    self.color('white')
    self.shape('square')
    self.turtlesize(0.5, 3)
    self.setheading(90)

  def up(self):
    if self.position()[1] > 250:
      return
    self.forward(20)

  def down(self):
    if self.position()[1] < - 250:
      return
    self.backward(20)