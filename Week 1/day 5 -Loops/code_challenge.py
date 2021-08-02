# You are going to write a program that calculates the average student height from a List of heights.

# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# e.g.

# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

# There are a total of 7 heights in student_heights

# 1146 ÷ 7 = 163.71428571428572

# Average height rounded to the nearest whole number = 164

# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: 156, 178, 165, 171, 187

# Example Output
# 171

# heights_arr = [180, 124, 165, 173, 189, 169, 146]
# total = 0

# for height in heights_arr:
#   total += height
  
# print(f"The average height is {round(total/len(heights_arr), 2)}")

##############################################################################

# Instructions
# You are going to write a program that calculates the highest score from a List of scores.

# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. The output words must match the example. i.e

# The highest score in the class is: x

# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output
# The highest score in the class is: 91

# scores_arr = [78, 65, 89, 86, 55, 91, 64, 89]
# curr_highest = 0

# for score in scores_arr:
#   if score>curr_highest:
#     curr_highest = score

# print(f"The highest score is {curr_highest}")

################################################################################

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# total = 0
# for number in range(0, 101, 2):
#   # total += number
#   if number % 2 == 0:
#     total += number

# print(total)

################################################################################


# You are going to write a program that automatically prints the solution to the FizzBuzz game.

# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
#   `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

# for number in range(1, 21):
#   if number % 5 == 0 and number % 3 == 0:
#     print('FizzBuzz')
#   elif number % 5 == 0:
#     print('Buzz')
#   elif number % 3 == 0:
#     print('Fizz')
#   else:
#     print(number)

# for number in range(1, 21):
#   print_str = ''
#   if number % 3 == 0:
#     print_str += 'Fizz'
#   if number % 5 == 0:
#     print_str += 'Buzz'
  
#   print(print_str or number)
