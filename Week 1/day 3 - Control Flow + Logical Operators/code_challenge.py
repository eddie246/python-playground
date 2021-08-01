# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.

# e.g. 86 is even because 86 ÷ 2 = 43

# 43 does not have any decimal places. Therefore the division is clean.

# e.g. 59 is odd because 59 ÷ 2 = 29.5

# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

# e.g.

# 6 ÷ 2 = 3 with no remainder.

# 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.

# 5 % 2 = 1
# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.

# 14 % 4 = 2
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 1
# 43
# Example Output 1
# This is an odd number.
# Example Input 2
# 94
# Example Output 2
# This is an even number.

# num = int(input('Input a number\n'))

# if num%2 == 0:
#   print('Your number is even.')
# else:
#   print('Your number is odd.')


################################################################################

# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

# Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

# Example Input
# weight = 85
# height = 1.75
# Example Output
# 85 ÷ (1.75 x 1.75) = 27.755102040816325

# Your BMI is 28, you are slightly overweight.

# weight = float(input("Please enter your weight in kg. \n"))
# height = float(input("Please enter your height in m.\n"))

# bmi = float("{:.2f}".format(weight/height**2))

# if bmi < 18.5:
#   print("You are underweight")
# elif bmi < 25:
#   print("You have a normal weight")
# elif bmi < 30:
#   print("You are overweight")
# elif bmi < 35:
#   print('You are obese')
# else:
#   print('You are clinically obese')

################################################

# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)

# 2000 ÷ 100 = 20 (Not Leap)

# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:

# 2100 ÷ 4 = 525 (Leap)

# 2100 ÷ 100 = 21 (Not Leap)

# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 1
# 2400
# Example Output 1
# Leap year.
# Example Input 2
# 1989
# Example Output 2
# Not leap year.

# year = int(input('Enter year: '))

# if year % 4 == 0:
#   if year % 400 == 0:
#       print(f"{year} is a leap year")
#   elif year % 100 == 0:
#     print(f"{year} is not a leap year")
#   else: print(f"{year} is a leap year")
# else: 
#   print(f"{year} is not a leap year")

#################################################

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.

# size = input("What size of pizza would you like? S M or L ")
# pep = input("Would you like pepperoni on your pizza? Y or N ")
# cheeze = input("Would you like extra cheese on your pizza? Y or N ")

# total = 0

# if size == 'S':
#   total += 10
#   if pep == 'Y': total += 2
#   if cheeze == 'Y': total += 1
# elif size == 'M':
#   total += 20
#   if pep == 'Y': total += 3
#   if cheeze == 'Y': total += 1
# else:
#   total += 25
#   if pep == 'Y': total += 3
#   if cheeze == 'Y': total += 1

# print(f"Your total is ${total}")

####################################################################

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

# e.g.

# name1 = "Angela Yu"

# name2 = "Jack Bauer"

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.

name1 = input('What is your name? ').lower()
name2 = input('What is their name? ').lower()

your_true = int(name1.count('t')) + int(name1.count('r')) + int(name1.count('u')) + int(name1.count('e'))
their_love = int(name1.count('l')) + int(name1.count('o')) + int(name1.count('v')) + int(name1.count('e'))

compatibility = int(str(your_true) + str(their_love))

if compatibility > 90 or compatibility < 10:
  print(f"Your score is {compatibility}, you go together like coke and mentos.")
elif compatibility > 40 and compatibility < 50:
  print(f"Your score is {compatibility}, you are alright together.")
else:
  print(f"Your score is {compatibility}")