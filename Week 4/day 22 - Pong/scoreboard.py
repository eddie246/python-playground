from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.speed('fastest')
    self.color('white')
    self.penup()
    self.hideturtle()
    self.player1 = -1
    self.player2 = 0

  def draw_middle(self):
    self.goto(0, -280)
    self.setheading(90)
    self.pencolor('white')
    for _ in range(10):
      self.pendown()
      self.forward(30)
      self.penup()
      self.forward(30)

  def update_score(self, player):
    player+= 1
    self.clear()
    self.goto(0, 290)
    self.write(f'Player 1 Score: {self.player1}                  Player 2 Score: {self.player2}', False, 'center', ('Aria', 12, 'normal'))
    # self.goto(200, 300)
    # self.write(f'Player 2 Score: {self.player2}')