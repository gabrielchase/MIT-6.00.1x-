# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    return set(secretWord) <= set(lettersGuessed)
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    letters = []
    
    # Better solution
    for letter in secretWord:
      if letter in lettersGuessed:
        letters.append(letter)
      else:
        letters.append('_')
    return ''.join(letters)
    
    # correct_letters = []
    # output_guess = ['_'] * len(secretWord)
    
    # for letter in lettersGuessed:
    #   if letter in secretWord:
    #     letter_indexes = [idx for idx, secretLetter in enumerate(secretWord) if secretLetter == letter]
        
    #     for idx in letter_indexes:
    #       output_guess[idx] = letter

    # return ''.join(output_guess)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    return ''.join(sorted(set(string.ascii_lowercase) - set(lettersGuessed))) 

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

    NUMBER_OF_GUESSES = 8
    guessed = False
    letters_guessed = []
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secretWord)))

    while not guessed:
      print('-------------')
      
      if NUMBER_OF_GUESSES <= 0:
        print('Sorry, you ran out of guesses. The word was {}'.format(secretWord))
        return
      
      print('You have {} guesses left'.format(NUMBER_OF_GUESSES))
      
      available_letters = getAvailableLetters(letters_guessed)

      print('Available letters: {}'.format(available_letters))
      
      guessed_letter = input('Please guess a letter: ')
      
      if guessed_letter in letters_guessed:
        print("Oops! You've already guessed that letter: {}".format(guessed_word))
      else:  
        letters_guessed.append(guessed_letter)
        guessed_word = getGuessedWord(secretWord, letters_guessed)
        
        if guessed_letter in secretWord:
          print('Good guess: {}'.format(guessed_word))
        
          if isWordGuessed(secretWord, letters_guessed):
            print('-------------')
            print('Congratulations, you won!')
            guessed = True
        else:
          print('Oops! That letter is not in my word: {}'.format(guessed_word))
          NUMBER_OF_GUESSES -= 1


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
