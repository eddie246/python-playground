import random
import os
import assets
import data_set

clear = lambda: os.system('cls')

def game(comp1, comp2, score=0):
  clear()
  print(assets.logo)

  print(f"Compare A: {comp1['name']}, a {comp1['description']}, from {comp1['country']}.")
  print(assets.vs)
  print(f"Compare B: {comp2['name']}, a {comp2['description']}, from {comp2['country']}.")

  guess = input("Who has more followers? Type 'a' or 'b': ")
  if guess == 'a' and comp1['follower_count'] > comp2['follower_count']:
    score += 1
    game(comp2, random.choice(data_set.data), score)
  elif guess == 'b' and comp2['follower_count'] > comp1['follower_count']:
    score += 1
    game(comp2, random.choice(data_set.data), score)
  else:
    if input(f'You lost... Your final score was: {score}. Would you like to try again? y or n: ') == 'y':
      game(random.choice(data_set.data), random.choice(data_set.data))
  return

game(random.choice(data_set.data), random.choice(data_set.data))