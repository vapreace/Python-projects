#! /usr/bin/python
# **************************************************************************** #
#                                                                              #
#   -- hangman_game.py --                                       /`·.¸          #
#                                                              /¸...¸`:·       #
#   By: ines_lemos                                         ¸.·´  ¸   `·.¸.·´)  #
#   Github: github.com/vapreace                           : © ):´;      ¸  {   #
#   Linkedin: https://www.linkedin.com/in/ines-s-lemos/    `·.¸ `·  ¸.·´\`·¸)  #
#   Last updated: 2024-08-09                                   `\\´´\¸.·´      #
#                                                                              #
# **************************************************************************** #

"""
Hangman Game
------------
This script implements a simple hangman game. The player must guess a word
randomly chosen from a list of Portuguese words. The player has a limited
number of attempts to guess all the letters in the word before being "hanged".

Modules:
    random: To choose a random word from the list.
    words: Contains the list of Portuguese words.
    pics: Contains the hangman game images, game over message, and victory message.
"""

import random
from words import words_in_portuguese
from pics import hangman_pics, game_over, victory

word_in_use = random.choice(words_in_portuguese).upper() # Random word to be guessed
letters_to_guess = set(word_in_use) # Set of unique letters in the word
guessed_letters = set() # Set of correctly guessed letters
failed_letters = [] # List of incorrectly guessed letters (to be displayed)
max_attempts = len(hangman_pics) - 1 # Maximum number of attempts
tries = 0 # Number of attempts made by the user

while tries <= max_attempts and len(letters_to_guess) >= 0:
    if max_attempts - tries == 0: # If the user has no more attempts, game over
        print(hangman_pics[tries])
        print(game_over)
        print("\nYou lost! The word was:", word_in_use)
        break

    if len(letters_to_guess) == 0: # If the user guesses all the letters, victory
        print(hangman_pics[tries])
        print(victory)
        print("\nYou won! The word was:", word_in_use)
        break

    print(hangman_pics[tries]) # Display the current state of the hangman
    
    print("Current word: ", end="") # Display the current state of the word
    for letter in word_in_use:
        if letter in guessed_letters:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")
            
    print("\nIncorrect guesses: ", end="") # Display the incorrect guesses
    print(" ".join(failed_letters).upper())

    guess = input("Guess a letter: ").upper() # Ask the user to guess a letter
    
    if not guess.isalpha() or len(guess) != 1: # Validate the input
        print("\nInvalid input. Please enter a single letter.")
        continue
    
    if guess in guessed_letters or guess in failed_letters: # Check if the letter was already guessed
        print("\nYou already guessed that letter.")
        
    elif guess in letters_to_guess: # Check if the letter is in the word
        letters_to_guess.remove(guess)
        guessed_letters.add(guess)
        
    else: # If the letter is not in the word
        tries += 1
        failed_letters.append(guess)