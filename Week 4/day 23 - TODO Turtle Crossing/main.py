# file = open('Week 4/day 23 - TODO Turtle Crossing/test.txt')
# contents = file.read()
# print(contents)
# file.close()

with open('C:/Users/Eddie/Desktop/python-playground/Week 4/day 24 - File System/test.txt') as file:
  contents = file.read()
  print(contents)

with open('C:/Users/Eddie/Desktop/python-playground/Week 4/day 24 - File System/test.txt', 'a') as file2:
  file2.write("hello\n")
  