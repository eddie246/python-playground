student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato = pandas.read_csv('C:/Users/Eddie/Desktop/python-playground/Week 4/day 26 - List Comprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter: row.code for (_, row) in nato.iterrows()}
print(nato_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Please enter your word: ").upper()
word_coded = [nato_alphabet[letter] for letter in user_word if letter in nato_alphabet]
print(word_coded)