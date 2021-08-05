import assets
import os
import random
clear = lambda: os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(assets.logo)

def blackjack():
  player_cards = []
  player_total = 0
  for _ in range(2):
    card = random.choice(cards)
    player_total += card
    player_cards.append(card)

  print(f"   Your cards: {player_cards}, current score: {player_total}")

  computer_cards = []
  computer_total = 0

  for _ in range(2):
    card = random.choice(cards)
    computer_total += card
    computer_cards.append(card)

  print(f"   Computer's first card: {computer_cards[0]}")

  continue_blackjack = True

  while continue_blackjack:
    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
      card = random.choice(cards)
      player_total += card
      player_cards.append(card)
      if computer_total < 17:
        card = random.choice(cards)
        computer_total += card
        computer_cards.append(card)
      print(f"   Your cards: {player_cards}, current score: {player_total}")
      print(f"   Computer's first card: {computer_cards[0]}")
      if player_total > 21 and 11 in player_cards:
        player_total -= 10
        player_cards.remove(11)
        player_cards.append(1)
      elif player_total > 21:
        continue_blackjack = False
        print(f'You lost!')
        if input('Do you want to play a game of blackjack? y or n: ') == 'y':
          return blackjack()
    else:
      continue_blackjack = False
      print(f"   Your cards: {player_cards}, current score: {player_total}")
      print(f"   Computer cards: {computer_cards}, current score: {computer_total}")
      
      if player_total > computer_total:
        print(f'You won! You have {player_total} against {computer_total}')
      else:
        print('You lost!')
      if input('Do you want to play a game of blackjack? y or n: ') == 'y':
        return blackjack()

blackjack()