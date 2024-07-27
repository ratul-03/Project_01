'''
1 for snake
-1 for water
0 for gun
'''

import random

# Generate a random choice for the computer
computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice (s for snake, w for water, g for gun): ")
youDict = {'s': 1, 'w': -1, 'g': 0}

# Check if the input is valid
if youStr in youDict:
    you = youDict[youStr]

    if computer == you:
        print("Game Tie")
    else:
        if (computer == -1 and you == 1):
            print("You win the game")
        elif (computer == -1 and you == 0):
            print("You Lose 😔")
        elif (computer == 1 and you == -1):
            print("You lose 😔")
        elif (computer == 1 and you == 0):
            print("You win the game")
        elif (computer == 0 and you == 1):
            print("You Lose 😔")
        elif (computer == 0 and you == -1):
            print("You win the game")
        else: 
            print("Something is wrong")
else:
    print("Invalid input! Please enter 's', 'w', or 'g'.")