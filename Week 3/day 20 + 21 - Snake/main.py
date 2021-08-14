from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    scoreboard.game_over()
  if snake.snake_body[0].distance(food) < 1:
    food.move_food()
    scoreboard.inc_score()
    snake.make_body()

  for body in snake.snake_body[1:]:
    if snake.snake_body[0].distance(body) < 10:
      game = False
      scoreboard.game_over()
    if body.distance(food) < 15:
      food.move_food()

screen.exitonclick()