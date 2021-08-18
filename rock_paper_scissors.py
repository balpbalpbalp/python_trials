# Rock Paper Scissors

# Pseudocode

# 0. The list of options is comprised of Rock, Paper, and Scissors.
# 1. The computer is assigned one random option from the list: Rock, Paper, and Scissors while the player is out of the game.
# 2. The player is asked to choose one specific option from the list: Rock, Paper, and Scissors.
# 3. The two options are compared:
#   3.1. If the two options are the same, the game is a tie.
#   3.2. If the two options are not the same:
#       3.2.1. Rock beats Scissors and loses to Paper.
#       3.2.2. Scissors beats Paper and loses to Rock.
#       3.2.2. Paper beats Rocks and loses to Scissors.
# 4. Ask if the player wants to continue playing and act accordingly.

# Code

from random import randint

# 0. 

options = ["1", "2", "3"]

# 1.

computer = options[randint(0, 2)]
player = False

# 2.

while player == False:

    print("Good luck.")
    player = input("1 for Rock, 2 for Paper, or 3 for Scissors? ")

   # 3.

   # 3.1.
    
    if player == computer:
        print("It is a tie.")

    # 3.2.

    # 3.2.1.

    elif player == "1":
        if computer == "3":
            print("The player wins.")
        else:
            print("The computer wins.")

    # 3.2.2

    elif player == "2":
        if computer == "1":
            print("The player wins.")
        else:
            print("The computer wins.")

    # 3.2.3

    elif player == "3":
        if computer == "2":
            print("The player wins.")
        else:
            print("The computer wins.")

    else:
        print("That is a not valid option in this game.")
    
    # 4.

    player = input("Would you like to play again, 1 for Yes or 2 for No? ")
    if player == "1":
        player = False
        computer = options[randint(0, 2)]
    
    elif player == "2":
        print("Thanks for playing, bye bye.")
        break

    else:
        print("Invalid option, bye bye.")