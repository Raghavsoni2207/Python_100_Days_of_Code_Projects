import random
import Day7_HangmanWords
import Day7_HangmanArt

# Printing logo imported through Day7_HangmanArt file
print(Day7_HangmanArt.logo)

# Lives and corresponding stages imported from Day7_HangmanArt file
lives = 6
stages = Day7_HangmanArt.stages

# Importing list of words from hangmanWords file
words = Day7_HangmanWords.word_list

# Setting the game run true
game_status = True

# Choosing a random word from words list
word = random.choice(words)
#print(word)

# Creating blanks according to word
guess_list = []
for i in range(len(word)):
    guess_list.append("_")

# Continues game tracking the end through game_statis
while game_status:
    # Taking input of user guess letter
    user_letter = input("Guess the letter? ").lower()

    # To check the repeatability of user guess letter
    if user_letter in guess_list:
        print("You've already guessed " + user_letter)
    else:
        for j in range(len(word)):
            if word[j] == user_letter:
                guess_list[j] = user_letter

    # If the letter is not correct then deducting one life
    if user_letter not in guess_list:
        print("You guessed " + user_letter + ", that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You Lose.")
            game_status = False

    # printing the guess_list in format
    print(f"{' '.join(guess_list)}")

    # Checking if the user win or not
    if "_" not in guess_list:
        print("You Win.")
        game_status = False

    #   Printing the stages
    print(stages[lives])
