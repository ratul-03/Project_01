# Snake-Water-Gun Game

This project is a simple command-line implementation of the classic Snake-Water-Gun game using Python. The game allows you to play against the computer, which makes a random choice each round.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [License](#license)

## Installation

To get started with this project, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```sh
   git clone <repository-url>
Navigate to the project directory:
sh
Copy code
cd snake-water-gun
Usage
To play the game, run the Python script:

sh
Copy code
python game.py
You will be prompted to enter your choice for each round. The options are:

s for Snake
w for Water
g for Gun
Game Rules
Snake drinks water: Snake (1) vs Water (-1) -> You win
Water douses gun: Water (-1) vs Gun (0) -> You lose
Gun shoots snake: Gun (0) vs Snake (1) -> You lose
If both players choose the same option, the game is a tie.
Here is the code for the game:

python
Copy code
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
License
This project is licensed under the ISC License.
My repository url: https://github.com/ratul-03/Project_01. This README provides an overview of the project, how to install and run it, the game rules, and includes the game's Python code.
