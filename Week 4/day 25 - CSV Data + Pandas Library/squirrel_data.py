import pandas

squrrels = pandas.read_csv('C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_count = len(squrrels[squrrels['Primary Fur Color'] == 'Gray'])
red_count = len(squrrels[squrrels['Primary Fur Color'] == 'Cinnamon'])
black_count = len(squrrels[squrrels['Primary Fur Color'] == 'Black'])

print(gray_count, red_count, black_count)

squrrels_pop = {
  'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
  'Count': [gray_count, red_count, black_count]
}

squrrels_dataframe = pandas.DataFrame(squrrels_pop)
squrrels_dataframe.to_csv('C:/Users/Eddie/Desktop/python-playground/Week 4/day 25 - CSV Data + Pandas Library/2018 Central Park Squrrel Counts.csv')