import random
import assets
import wordbank

print(f'{assets.logo}\nWelcome to Handman!')

chosen_word = random.choice(wordbank.word_list) 

curr_guess = []
curr_lives = 6

for _ in chosen_word:
  curr_guess.append('_')

while (''.join(curr_guess) != chosen_word):
  guess = input(f'You have {curr_lives} lives. Enter a random letter: ').lower()
  for number in range(0, len(chosen_word)):
    if chosen_word[number] == guess:
      curr_guess[number] = guess
      print(assets.stages[curr_lives])
  if not guess in chosen_word:
    curr_lives -= 1
    print(assets.stages[curr_lives])
    if curr_lives < 1:
      print(f'You Ran Out of Lives. You Lost! The Word Was: {chosen_word}')
      break
  
  print(' '.join(curr_guess))

if not '_' in curr_guess:
  print(f'You won! the word was: {chosen_word}')

