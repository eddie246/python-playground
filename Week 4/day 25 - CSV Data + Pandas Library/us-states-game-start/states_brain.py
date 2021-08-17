from turtle import Turtle
import pandas

STATES_DATA = 'C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/us-states-game-start/50_states.csv'

class State_Game(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.correct_guesses = []
    self.all_states = pandas.read_csv(STATES_DATA)

  def check_state(self, state):
    if state in self.correct_guesses:
      return "already guessed"
    else:
      data_in_csv = self.all_states[self.all_states.state == state.title()]
      if len(data_in_csv) == 1:
        self.correct_guesses.append(state.title())
        self.goto(int(data_in_csv.x), int(data_in_csv.y))
        self.write(data_in_csv.state.item())
        return data_in_csv
      return 'Incorrect'
  
  def gen_unguessed(self):
    states_unguessed = {
      'States' : []
    }
    for state in self.all_states.state.to_list():
      if state not in self.correct_guesses:
        states_unguessed['States'].append(state)
    
    print(states_unguessed['States'])
    # for state in self.all_states.to_dict()['state']:
    #   if self.all_states.to_dict()['state'][state] not in self.correct_guesses:
    #     states_unguessed['States'].append(self.all_states.to_dict()['state'][state])
    
    states_unguessed_csv = pandas.DataFrame(states_unguessed)
    states_unguessed_csv.to_csv('C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/us-states-game-start/states_not_guessed.csv')
