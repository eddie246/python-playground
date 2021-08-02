# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# e.g.
# 1 means Heads
# 0 means Tails

# Example Output
# Heads
# or
# Tails

import random

random_int = random.randint(0, 1)

if random_int == 0:
  print('Head')
else:
  print('Tails')

###################################################################

# Instructions
# You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# names_str = input('Please enter names seperated by a comma and a space: ')
# names_arr = names_str.split(', ')

# random_choice = names_arr[random.randint(0, len(names_arr)-1)]
# print(f"{random_choice} was selected at random!")

# # Alternatively: 

# random_choice_method = random.choice(names_arr)
# print(f"{random_choice_method} was selected at random!")

###############################################################################

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

row = int(position[0])
col = int(position[1])

map[row-1][col-1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")