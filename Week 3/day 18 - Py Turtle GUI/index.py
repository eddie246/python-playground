from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.shape('turtle')
timmy.color('black', 'green')

# for number in range(3, 11):
#   for repeat in range(number):
#     timmy.forward(100)
#     timmy.right(360/number)
timmy.pensize(1)
timmy.speed('fastest')

# for walk in range(101):
#   timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#   timmy.setheading(random.choice([0, 90, 180, 270]))
#   timmy.forward(50)

for circle in range(180):
  timmy.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  timmy.circle(100)
  timmy.right(2)



screen.exitonclick()