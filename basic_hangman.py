import os

def get_word():
    global enter_word
    enter_word = str(input("Enter a word: ")).lower()
    return enter_word

get_word()
os.system("clear")

def play_hangman():
    word = enter_word
    letters_guessed = []
    number_of_tries = 10
    guessed = False

    print(f"The word has {len(word)} letters.")
    print(" _ " * len(word))

    while guessed == False and number_of_tries > 0:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        print(f"You have {number_of_tries} guesses left.")
        guess = str(input("Guess a letter or the whole word: ")).lower()

        # 1. User inputs a letter.

        if len(guess) == 1:
            if guess not in alphabet:
                print("You have not entered a letter.")
            elif guess in letters_guessed:
                print("You have already guessed this letter.")
            elif guess not in word:
                print("The letter is not in the word.")
                letters_guessed.append(guess)
                number_of_tries -= 1
            elif guess in word:
                print("The letter is in the word.")
                letters_guessed.append(guess)
            else:
                print("Error.")

        # 2. User inputs a whole word.

        if len(guess) == len(word):
            if guess == word:
                print("Well done, you have correctly guessed the word!")
                guessed = True
            else:
                print("The guess is incorrect.")
                number_of_tries -= 1

        # 3. User inputs more than letter he/she should.

        if len(guess) > len(word):
            print("The entry is invalid because you have entered too many characters.")
            number_of_tries -= 1

        status = ""
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += "_"
            print(status)
        
        if status == word:
            print("Well done, you have correctly guessed the word!")
            guessed = True

        elif number_of_tries == 0:
            print("You have run out of tries.")

    play_again()

def play_again():
    play_again_question = int(input("Would you like to play again? (Press 1 to play again - Press 2 to close the game."))
    
    if play_again_question == 1:
        get_word()
        os.system("clear")
        play_hangman()
    
    elif play_again_question == 2:
        print("Bye bye.")
        quit()

    else:
        print("Invalid entry.")

play_hangman()