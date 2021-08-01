# print(len('hello'))
# #print(len(123)) # will throw type error
# print(len(str(123)))
# print('Hello'[0])
# print('Hello'[len('hello')-1])

# # integer
# print('1' + '1')
# # print(1 + '1') #throws error, no type coersion like JS
# print(1 + 1)
# print(123_123_123) # can use _ in Int or Float to make number more readable

# # float
# print(1.1 + 1)

# # boolean
# print(True)

# # practice
# name_length = str(len(input('What is your name?\n')))

# print('Your name has ' + name_length + ' characters')
# print(type(name_length))

# a = 123

# # convert to String
# a = str(123)

# # convert to Float
# a = float(123)

# print(type(a))

# DIfferent math operations

# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3

# 2 ** 2

# print(round(8/3))
# print(round(8/3, 3))

# print(round(8//3)) #floor division: automatically cuts off the decimal; turn into int

# item = 6
# item /= 2

# print(item)

# # F-strings
# score = 234

# print(f"Your score is {score}")

# Tip Calculator

print('Welcome to the tip calculator.\n')
total = float(input('What was the total bill?\n'))
tip_percent = float(input('What percent tip would you like to give? 10, 12, or 15?\n'))/100
total_bill = total * tip_percent + total

split = int(input('How many people to split the bill?\n'))
each_person = round(total_bill / split, 2)
each_person = "{:.2f}".format(each_person)

print(f"Each person should pay: ${each_person}")
