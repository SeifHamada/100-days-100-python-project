import art
print(art.logo)

highest = 0
bidders = {}


def highest_bidder(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    again = input("Are there any other bidders? Type 'yes or 'no': ").lower()
    if again == "no":
        highest_bidder(bidders)
        break
    else:
        print("\n" * 100)


