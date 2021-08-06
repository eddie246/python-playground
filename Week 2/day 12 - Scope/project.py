import random
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

difficulty = input('Choose a difficulty, easy or hard: ')
ran_num = random.randint(1, 101)

if difficulty == 'easy':
  lives = 10
else:
  lives = 5

while lives > 0:
  print(f"You have {lives} attempts remaining to guess the number.")
  guess = int(input('Make a guess: '))

  lives -= 1
  if guess > ran_num:
    print('You guessed too high.')
  elif guess < ran_num:
    print('You guessed too low.')
  else:
    print('You guessed the correct number. You won!')
    lives = 0