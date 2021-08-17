import turtle
from states_brain import State_Game

IMAGE = 'C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/us-states-game-start/blank_states_img.gif'

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.setup(720, 490)
screen.listen()

screen.addshape(IMAGE)

turtle.shape(IMAGE)

game = State_Game()
in_progress = True

while len(game.correct_guesses) != 50 and in_progress:
  user_answer = screen.textinput(f'{len(game.correct_guesses)}/50 States Correct', "What is another state's name?")

  state_data = game.check_state(user_answer)
  if user_answer == 'end':
    in_progress = False
    game.gen_unguessed()

screen.exitonclick()