from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.hideturtle()
    self.color('white')
    self.goto(0, 275)
    self.score = 0
    self.write('Score: 0', False, 'center', ('Aria', 12, 'normal'))
  
  def inc_score(self):
    self.score+=1
    self.clear()
    self.write(f'Score: {str(self.score)}', False, 'center', ('Aria', 12, 'normal'))
    
  def game_over(self):
    self.goto(0,0)
    self.write('Game Over', False, 'center', ('Aria', 16, 'normal'))