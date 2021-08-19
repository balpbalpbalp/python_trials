# Number Guessing

# Pseudocode

# 0. The computer is assigned an arbitrary number.
# 1. Before the game, information regarding the player is asked.
#   1.1. Ask whether the player wants to take part in the game.
#       1.1.1. If so, ask for the player's name.
#       1.1.2. If not, print a bye-bye message.
# 2. Ask for a number between 1 and 10.
#   2.1. If the number is equal to the arbitrary number, print a victory message and give a positive score.
#   2.2. If the number is lower or higher than the arbitrary number, print "higher" or "lower" accordingly.
#   2.3. If the number is out of bounds, print a message indicating an invalid entry is given.
# 3. Finalize the results.

# Code

from random import randint 
number_of_attempts = []

def show_score():
    if len(number_of_attempts) <= 0:
        print("There is currently no high score.")
    else:
        print("The current high score is {}.".format(min(number_of_attempts)))

def start_game(): # 0.
    generate_random_number = randint(1, 10)
    print("Welcome the Number Guessing Game") # 1.
    player_name = input("What is your name? ")
    want_to_play_question = input("{}, welcome. Would you like to take part in the game? (Enter Yes / No) ".format(player_name))
    attempts = 0

    while want_to_play_question.lower() == "yes":
        try: # 2.
            guessed_number = int(input("Please make a guess between 1 and 10: "))
             # 3.
            if guessed_number > 10 or guessed_number < 1:
                raise ValueError("Please guess within the range.")
            
            if guessed_number == generate_random_number:
                print("Great, that is the correct guess.")
                attempts += 1
                number_of_attempts.append(attempts)
                print("It took you {} attempts to find the number.".format(attempts))
                play_again_question = input("Would you like to play again? (Enter Yes / No) ")
                attempts = 0
                show_score()
                generate_random_number = randint(1, 10)

                if play_again_question.lower() == "no":
                    print("Have a nice day!")
                    break

            elif guessed_number > generate_random_number:
                print("Incorrect, the number is lower.")
                attempts += 1

            elif guessed_number < generate_random_number:
                print("Incorrect, the number is higher.")
                attempts = +1

        except:
            pass

if __name__ == '__main__':
    start_game()