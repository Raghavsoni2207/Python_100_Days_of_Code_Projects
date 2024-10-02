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

choice = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
if user_choice>2:
    print("You typed invalid number, you lose!")
else:
    print(choice[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(choice[computer_choice])

    # Draw
    if user_choice == computer_choice:
        print("It's a draw!")
    # Win
    elif (user_choice == 0) and (computer_choice == 2):
        print("You Win!")
    elif (user_choice == 1) and (computer_choice == 0):
        print("You Win!")
    elif (user_choice == 2) and (computer_choice == 1):
        print("You Win!")
    # Lose
    else:
        print("You Lose!")
