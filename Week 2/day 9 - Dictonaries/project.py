import os
clear = lambda: os.system('cls')

all_bidders = {}

still_bidding = True

while still_bidding:
  name = input('Please enter your name: ')
  bid_amount = float(input('Enter you bid amount: '))

  all_bidders[name] = bid_amount

  if input('Are there any more bidder? Y or N: ') == 'Y':
    clear()
  else:
    still_bidding = False
    clear()
    highest = 0
    bidder = ''
    for key in all_bidders:
      if all_bidders[key] > highest:
        highest = "{:.2f}".format(all_bidders[key])
        bidder = key 
    print(f"The winner of the bid was {bidder} with a total of ${highest}")
    
    