"""
-------------------------------------------------------
Hangman Game
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2022-05-13"
-------------------------------------------------------
"""
# Imports
import random

# Constants

# contains all possible game board positions
GRAPHICS = [" GAME START...\n________      \n|      |      \n|             \n|             \n|             \n|             ", "\n________      \n|      |      \n|      0      \n|             \n|             \n|             ",
            "\n________      \n|      |      \n|      0      \n|      |      \n|             \n|             ", "\n________      \n|      |      \n|      0      \n|      |\     \n|             \n|             ", "\n________      \n|      |      \n|      0      \n|     /|\     \n|             \n|             ", "\n________      \n|      |      \n|      0      \n|     /|\     \n|       \     \n|             ", "\n________      \n|      |      \n|      0      \n|     /|\     \n|     / \     \n|             "]


def array_to_string(array):
    """
    --------------------------------------
    Converting array to string
    Use:  string = array_to_string(array)
    --------------------------------------
    Parameters:
        array - array to convert (list)
    Returns:
        string - string version of array (str)
    -------------------------------------------------------
    """
    string = ""
    for i in range(len(array)):
        string += array[i]
    return string


def get_word():
    """
    --------------------------------------
    Reads the word_list.txt file to create a list of strings and
    generates a random word based off a word_list index
    Use:  random_word = get_word()
    --------------------------------------
    Returns:
        random_word - random word in .txt file (str)
    -------------------------------------------------------
    """
    # creating list of words (list of str)

    word_list = []
    fv = open('word_list.txt', 'r')
    for line in fv:
        line = line.strip("\n")
        word_list.append(line)
    fv.close()

    # generating word based off index

    index = random.randint(0, len(word_list) - 1)
    random_word = word_list[index]

    return random_word


def game():
    """
    --------------------------------------
    Creating Hangman Game
    Use:  str_hidden_word, guesses = game()
    --------------------------------------
    Returns:
        str_hidden_word - number of spaces (_) required for the word (str)
        guesses - amount of guesses left (int)
    -------------------------------------------------------
    """

    random_word = get_word()

    # printing starting game board
    print(GRAPHICS[0])

    array = []
    inc_guess = 6
    graphic_count = 1

    # hiding randomly generated word with "_ _ _ ..."
    hidden_word = []
    for _ in range(len(random_word)):
        hidden_word.append("_ ")

    guess = str(input(f"Enter your guess (PRESS ENTER if done!): "))
    while inc_guess > 0 and len(array) <= len(random_word) and guess != "":
        guess = guess.lower()

        # if guess is correct
        if guess in random_word:
            for j in range(len(random_word)):
                if guess == random_word[j]:
                    hidden_word[j] = guess + " "
                    print(f"Answer: {array_to_string(hidden_word)}")
                    array.append(guess)
                    print(f"Number of Guesses Left: {inc_guess}")

        # if its not correct
        else:
            print(GRAPHICS[graphic_count])
            graphic_count += 1
            inc_guess -= 1
            print(f"Number of Guesses Left: {inc_guess}")

        # once the number of guesses hits 0
        if inc_guess > 0:
            guess = str(input(f"Enter your guess (PRESS ENTER if done!): "))
        else:
            print("Sorry you ran out of guesses! :( ")

    print()
    str_hidden_word = array_to_string(hidden_word)
    print(f"Winning Word: {random_word}")

    return str_hidden_word, inc_guess


# running program
str_hidden_word, guesses = game()
print(f"Answer: {str_hidden_word}")
print(f"Number of turns left: {guesses}")
