from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
purple = Turtle()

turtles = [red, orange, yellow, green, blue, purple]


user_bet = screen.textinput('Make a bet', 'Enter a color:')

for turtle in range(len(turtles)):
  turtles[turtle].penup()
  turtles[turtle].setposition(-200, -100 + turtle*40)

racing = True

def move_tick():
  global racing
  random.choice(turtles).forward(1)
  for turtle in turtles:
    position = turtle.position()
    if position[0] > 200:
      print(f"{turtle} is the winner")
      return False
  return True

while racing:
  if move_tick() == False:
    racing = False
  

screen.exitonclick()