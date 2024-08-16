from clear import clear
from art import logo
print(logo)

bids = {}
bid_finished = False

def higgest_bidder(bids):
    higgest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > higgest_bid:
            higgest_bid = bid_amount
            winner = bidder
    clear()      
    print(f"The winner is {winner} with bid amount of {higgest_bid}")        


while not bid_finished:
    name = input("What is your name? \n")
    bid = int(input("What is your bid?\n"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type'yes' or 'no'. ")
    if should_continue == "no":
        bid_finished = True
        higgest_bidder(bids)
    elif should_continue == "yes":
        clear() 