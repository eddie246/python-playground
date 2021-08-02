import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player = input('Choose between Rock, Paper, or Scissors: ').lower()
if player == 'rock':
  player = 0
elif player == 'paper':
  player = 1
else:
  player = 2

CPU = random.randint(0, 2)

print(f"Player chose: {choices[player]}\nCPU chose: {choices[CPU]}\n")

if CPU == player:
  print("It is a draw")
elif (player == 0 and CPU == 2) or (player == 1 and CPU == 0) or (player == 2 and CPU == 1):
  print("Player Wins!")
else:
  print("CPU Wins!")



