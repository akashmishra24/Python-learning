import os
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bidders = {}

def auction_bidding(bidder, amount):
  bidders[bidder] = amount
  
should_end = False
while not should_end:
  bidder = input("What is your name?: ")
  amount = int(input("What's your bid?: $"))
  auction_bidding(bidder, amount)
  restart = input("Are there are any other bidders? Type 'yes' or 'no'.\n")
  if restart == "yes":
    os.system("clear")
    print(logo)
    continue
  else:
    should_end = True
    
highest_bid = 0
name = ""
for key in bidders:
  if highest_bid < bidders[key]:
    highest_bid = bidders[key]
    name = key

print(f"The winner is {name} with a bid of ${highest_bid}")


  
  