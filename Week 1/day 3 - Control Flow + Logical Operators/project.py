print('Welcome to Treature Island. Your mission is to find the treasure.')

choice = input('You encounter a forked road. Do you go left or right? ')

if choice == 'left':
  choice = input('You go left and find yourself in front of a lake. Do you swim or wait? ')
  if choice == 'wait':
    choice = input('You wait for a boat which takes you to a set of door. Do you open the red door or the blue door or the yellow door? ')
    if choice == 'yellow':
      print('Congrats, you found the treasure')
    elif choice == 'red':
      print('You died in a fire, Game Over')
    else:
      print('You got eaten by beasts, Game Over.')
  else: 
    print('You were atttacked by a trout and died. Game Over')
else:
  print('You stepped into a trap. Game Over.')