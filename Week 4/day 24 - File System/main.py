# file = open('Week 4/day 23 - TODO Turtle Crossing/test.txt')
# contents = file.read()
# print(contents)
# file.close()

with open('test.txt') as file:
  contents = file.read()
  print(contents)

with open('test.txt', 'a') as file2:
  file2.write("anghoianeohga")