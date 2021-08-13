from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.pensize(1)
timmy.speed('fast')

def move():
  timmy.forward(1)

def back():
  timmy.backward(1)

def turn_left():
  timmy.left(1)

def turn_right():
  timmy.right(1)

def clear():
  timmy.clear()
  timmy.penup()
  timmy.home()
  timmy.pendown()

screen.listen()
screen.onkeypress(move, 'w')
screen.onkeypress(back, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(clear, 'c')



screen.exitonclick()