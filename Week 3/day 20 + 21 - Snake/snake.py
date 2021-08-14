from turtle import Turtle

class Snake:
  def __init__(self):
    self.snake_body = []
    self.make_body()
    self.make_body()
    self.make_body()
    self.game = True
    self.heading = 'right'

  def make_body(self):
    body = Turtle()
    body.shape('square')
    body.color('white', 'green')
    body.penup()
    if (len(self.snake_body) == 0):
      body.goto(0, 0)
    else:
      last_body = self.snake_body[len(self.snake_body) - 1]
      body.goto(last_body.pos()[0], last_body.pos()[1])
    self.snake_body.append(body)

  def left(self):
    if not self.heading == 'right':
      self.snake_body[0].setheading(180)
      self.heading = 'left'

  def right(self):
    if not self.heading == 'left':
      self.snake_body[0].setheading(0)
      self.heading = 'right'

  def up(self):
    if not self.heading == 'down':
      self.snake_body[0].setheading(90)
      self.heading = 'up'

  def down(self):
    if not self.heading == 'up':
      self.snake_body[0].setheading(270)
      self.heading = 'down'

  def move_snake(self):
    for segment in range(len(self.snake_body) - 1, -1, -1):
      if segment == 0:
        self.snake_body[segment].forward(20)
      else:
        self.snake_body[segment].goto(self.snake_body[segment - 1].position())