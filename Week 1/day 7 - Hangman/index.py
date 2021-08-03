import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list) 

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.



#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

curr_guess = []
print(chosen_word)

for letter in chosen_word:
  curr_guess.append('_')

curr_word = ' '.join(curr_guess)

while (curr_word != chosen_word):
  print(' '.join(curr_guess))
  guess = input('Enter a random letter: ').lower()
  for number in range(0, len(chosen_word)):
    if chosen_word[number] == guess:
      curr_guess[number] = guess

