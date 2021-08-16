#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('C:/Users/Eddie/Desktop/python-playground/Week 4/day 24 - File System/Mail Merge Project Start/Input/Names/invited_names.txt') as name_file:
    names_list = name_file.read().split('\n')

with open('C:/Users/Eddie/Desktop/python-playground/Week 4/day 24 - File System/Mail Merge Project Start/Input/Letters/starting_letter.txt') as template:
    letter_template = template.read()

for name in names_list:
    letter_name = letter_template.replace('[name]', name)
    with open(f'C:/Users/Eddie/Desktop/python-playground/Week 4/day 24 - File System/Mail Merge Project Start/Output/ReadyToSend/{name}.txt', 'w') as letter:
        letter.write(letter_name)