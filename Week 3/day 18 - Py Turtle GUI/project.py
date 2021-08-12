from turtle import Turtle, Screen
import random
from colors import colors_list

timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.speed('fastest')
timmy.penup()
timmy.setposition(-300, -300)
timmy.hideturtle()

for row in range(10):
  for col in range (10):
    timmy.dot(20, random.choice(colors_list))
    timmy.forward(50)
  timmy.setposition(-300, timmy.position()[1]+50)

screen.exitonclick()