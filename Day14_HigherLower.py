import random
import Day14_art
from Day14_game_data import data

def check(user_input, a_followers, b_followers):
    if a_followers > b_followers and user_input == 'a':
        return True
    elif b_followers > a_followers and user_input == 'b':
        return True
    else:
        return False

def game(optionA, optionB):
    status = True
    score = 0

    while status:
        # Display art logo
        print(Day14_art.logo)

        if score != 0:
            print(f"You're right! Current score: {score}")

        # printing option A
        print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}")
        followers_of_a = optionA['follower_count']

        print(Day14_art.vs)

        # printing option B
        print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}")
        followers_of_b = optionB['follower_count']

        # user input
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        # check user input
        # Update options for next round
        if check(user_input, followers_of_a, followers_of_b):
            score += 1
            optionA = optionB
            optionB = random.choice(data)
            while optionA == optionB:
                optionB = random.choice(data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            status = False

# Initial random data generate
# creating option_a
option_a = random.choice(data)
# creating option_b
option_b = random.choice(data)

# Both option should be different
while option_a == option_b:
    option_b = random.choice(data)

game(option_a, option_b)
