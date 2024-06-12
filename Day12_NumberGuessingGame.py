import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_dificulty():
    level = input("Chose a dificulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS

# Function to check user guess and answer
def check_answer(guess, answer, turns):
    """Check answer against guess and returns number of turns left"""
    if guess > answer:
        print("Too high")
        return  turns-1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

# Choosing a random number between 1 - 100
answer = random.randint(1, 100)

def game():
    turns = set_dificulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # User guessing a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

game()
