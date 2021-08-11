from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.color('black', 'green')

# for number in range(3, 11):
#   for repeat in range(number):
#     timmy.forward(100)
#     timmy.right(360/number)
timmy.pensize(5)
timmy.speed('fast')

for walk in range(101):
  timmy.pencolor(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
  timmy.setheading(random.choice([0, 90, 180, 270]))
  timmy.forward(50)


screen = Screen()
screen.exitonclick()