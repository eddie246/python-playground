import random
import pandas

numbers = [1 ,2 , 3]
new_list = []
for number in numbers:
  new_list.append(number + 1)
print(new_list)

new_list_comprehension = [number + 1 for number in numbers]
print(new_list_comprehension)

doubled = [number * 2 for number in range(1, 5)]
print(doubled)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_names = [name for name in names if len(name)<= 4]
caps_names = [name.upper() for name in names if len(name)>4]
print(new_names)
print(caps_names)

students = {name: random.randint(0, 100) for name in names}
print(students)

passed_students = {student: grade for (student, grade) in students.items() if grade >= 65}
print(passed_students)

students = {
  'students' : ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'],
  'scores': [random.randint(0, 100) for _ in names]
}

student_dataframe = pandas.DataFrame(students)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
  print(row.scores)