from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.listen()
screen.setup(800, 630)
screen.bgcolor('black')

scoreboard = Scoreboard()
scoreboard.update_score(scoreboard.player1)
line = Scoreboard()
line.draw_middle()

paddle1 = Paddle()
paddle1.setpos(-380, 0)

screen.onkeypress(paddle1.up, 'w')
screen.onkeypress(paddle1.down, 's')

paddle2 = Paddle()
paddle2.setpos(380, 0)

screen.onkeypress(paddle2.up, 'Up')
screen.onkeypress(paddle2.down, 'Down')

ball = Ball()
screen.onkey(ball.bounce, 'f')

in_game = True

while in_game:
  # time.sleep(0.001)
  ball.move_ball()
  if ball.ycor() > 285 or ball.ycor() < -285:
    ball.bounce()
  if ball.xcor() < -400 or ball.xcor() > 400:
    ball.reset()
  if ball.position()[0] < -370 and ball.ycor() < paddle1.ycor() + 30 and ball.ycor() > paddle1.ycor() - 35:
    ball.bounce()
  if ball.position()[0] > 370 and ball.ycor() < paddle2.ycor() + 30 and ball.ycor() > paddle2.ycor() - 35:
    ball.bounce()

screen.exitonclick()