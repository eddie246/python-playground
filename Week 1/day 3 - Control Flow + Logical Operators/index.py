print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm?\n'))
bill = 0

if height >= 120:
  age = int(input('What is your age?'))

  if age <12:
    print('Your ticket is $7.')
    bill += 7
  elif age<16:
    print('Your ticket is $8.')
    bill += 8
  else:
    print('Your ticket is $12')
    bill += 12

  ticket = input("Do you want a photo taken? Enter Y or N. ")
  if ticket == 'Y':
    bill += 3
    print(f"Photos will be taken. Your total is ${bill}")

else:
  print('You cannot ride the rollercoaster')