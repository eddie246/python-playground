# import csv

# with open('C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/weather_data.csv') as data:
#   weather_data = csv.reader(data)
#   temperature = []
#   for row in weather_data:
#     if row[1] == 'temp':
#       continue
#     temperature.append(int(row[1]))

# print(temperature)

import pandas

# access and read CSV data using pandas library
data = pandas.read_csv('C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/weather_data.csv')

# convert CSV dataframe into python object
# data_dict = data.to_dict()
# print(data_dict)

# conver CSV series into python object list
# temp = data['temp'].to_list()
# average = sum(temp) / len(temp)
# print(average)

# using methods on series and dataframe
# average_temp = data['temp'].mean()
# print(average_temp)

# max_temp = data['temp'].max()
# print(max_temp)

# selecting row by a value
# monday = data[data.day == 'Monday']
# print(int(monday.temp)*(9/5) + 32)

# hottest_day = data[data.temp == data.temp.max()]
# print(hottest_day)

# creating a dataframe
student_dict = {
  'student': ['Amy', 'James', 'Angela'],
  'score': [76, 56, 65]
}

student = pandas.DataFrame(student_dict)
student.to_csv('C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/student_data.csv')