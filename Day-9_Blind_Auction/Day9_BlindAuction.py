logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

def finding_highest_bid(bidding_record):
    highest_bidder = ""
    highest_bid = 0

    for key in bidding_record:
        if highest_bid < bidding_record[key]:
            highest_bidder = key
            highest_bid = bidding_record[key]

    print(f"The winner is {highest_bidder} with a bid of ${bidding_record[highest_bidder]}.")


auction_status = True
bids = {}

while auction_status:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    status = input("Are there any other bidders? 'yes' or 'no'.\n").lower()

    bids[name] = bid

    if status == "no":
        auction_status = False
        finding_highest_bid(bids)
