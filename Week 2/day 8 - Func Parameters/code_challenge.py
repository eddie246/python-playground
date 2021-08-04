# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 ✖️ 4) ÷ 5

#                      = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input
# test_h = 3
# test_w = 9
# Example Output
# You'll need 6 cans of paint.

# import math

# def calc_cans(height, width):
#   area = height * width
#   cans_required = math.ceil(area/5)
#   print(f"You need {cans_required} cans of paint.")

# calc_cans(int(input('Enter height: ')), int(input('Enter wdith: ')))

#######################################################################

# Prime numbers are numbers that can only be cleanly divided by itself and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H

# Here are the numbers up to 100, prime numbers are highlighted in yellow:

# https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw

# Example Input 1
# 73
# Example Output 1
# It's a prime number.

def prime_checker(num):
  is_prime = True
  for i in range(2, num+1):
    if num % i == 0 and num != i:
      is_prime = False
      break
  if is_prime:
    print('Prime number')
  else:
    print('Not Prime')

prime_checker(8)
prime_checker(13)
prime_checker(71)
prime_checker(137)
prime_checker(71)