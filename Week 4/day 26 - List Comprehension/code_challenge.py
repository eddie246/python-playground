# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.

# e.g. `4 * 4 = 16`
# 4 squared equals 16.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# You are going to write a List Comprehension to create a new list called result. This new list should only contain the even numbers from the list numbers.

# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a Loop.

# Example Output
# [2, 8, 34]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number % 2 == 0]
print(result)

# Instructions
# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

# e.g. if file1.txt contained:

# 1
# 2
# 3
# and file2.txt contained:

# 2
# 3
# 4
# result = [2, 3]

with open('C:/Users/Eddie/Desktop/python-playground/Week 4/day 26 - List Comprehension/file1.txt') as file1nums:
  file1 = [int(number) for number in file1nums.read().split('\n') if number != '']

with open('C:/Users/Eddie/Desktop/python-playground/Week 4/day 26 - List Comprehension/file2.txt') as file1nums:
  file2 = [int(number) for number in file1nums.read().split('\n') if number != '']

common_nums = [number for number in file1 if number in file2]
print(common_nums)

##################################################################################################################

# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

# Try Googling to find out how to convert a sentence into a list of words.

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split(' ')

result = {word: len(word) for word in sentence}
print(result)

# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)