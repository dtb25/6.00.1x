# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:26:38 2016

@author: David
"""

#
# Recursive helper function #1 for hangman game
#

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(secretWord) <= 1: return secretWord in lettersGuessed
    return secretWord[0] in lettersGuessed and isWordGuessed(secretWord[1:], lettersGuessed)
    
#%%

#
# Recursive helper function #2 for hangman game
#
  
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if len(secretWord) <= 1:
        if secretWord in lettersGuessed: return secretWord
        return '_ '
    if secretWord[0] in lettersGuessed: 
        return secretWord[0] + getGuessedWord(secretWord[1:], lettersGuessed)
    return '_ ' + getGuessedWord(secretWord[1:], lettersGuessed)

#%%

#
# Helper function #3 for hangman game
#

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    output = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in lettersGuessed: output += letter
    return output

#%%%

#
# The hangman game - a long string of conditionals!
#

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 0
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %s letters long.' % len(secretWord))
    while mistakesMade < 8:
        print('-------------')
        print('You have %s guesses left.' % (8 - mistakesMade))
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        guess = guess.lower()
        #        
        # first handle the possibility that the player's input is invalid
        #
        if len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Oops! I can't understand your guess!"),
            print('Please enter a single letter and then press return')
        #
        # Now check to see if the player has already guessed the letter
        # they typed
        #
        elif guess in lettersGuessed: 
            print("Oops! You've already guessed that letter: "),
            print(getGuessedWord(secretWord, lettersGuessed))
        #
        # Handle the case where the input is valid and not previously
        # guessed but not in the secret word
        #
        elif guess not in secretWord:
            lettersGuessed.append(guess)
            mistakesMade += 1
            print("Oops! That letter is not in my word: "),
            print(getGuessedWord(secretWord, lettersGuessed))
        #
        # Finally, the case where the input is valid, not previously guessed,
        # and in the secret word
        #
        else: 
            lettersGuessed.append(guess)
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
                print('------------')
                print('Congratulations, you won!')
                break
    if mistakesMade >= 8:
        print('------------')
        print('Sorry, you ran out of guesses. The word was ' + secretWord)    
                 