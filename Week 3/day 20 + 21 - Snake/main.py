from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

screen.listen()

screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.make_body, 'space')

game = True

while game:
  time.sleep(0.1)
  snake.move_snake()
  screen.update()
  if snake.snake_body[0].position()[0] > 300 or snake.snake_body[0].position()[0] < -300 or snake.snake_body[0].position()[1] > 300 or snake.snake_body[0].position()[1] < -300:
    game = False

screen.exitonclick()