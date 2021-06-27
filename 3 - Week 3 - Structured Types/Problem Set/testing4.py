# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
cls = lambda: print("\033[2J\033[;H", end='')
cls()

import random

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

# end of helper code
# -----------------------------------

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
    # FILL IN YOUR CODE HERE...
    totallen = len(secretWord)
    for i in lettersGuessed:
        totallen -= secretWord.count(i)       
    if totallen <= 0:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    listi = []
    # Turn string into list
    for i in secretWord:
        listi += i   
    # See if each letter has been guessed, replaced for _
    for idx,val in enumerate(listi):
        if val not in lettersGuessed:
            listi[idx] = '_ '    
    final = ''
    # Turn back into string
    for i in listi:
        final += i[0:2]
    return final

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letters = string.ascii_lowercase
    
    # Turn string into list
    listi = []
    for i in letters:
        listi += i   
    
    # Delete values from list
    listcopy = listi[:]
    for letter in listcopy:
        if letter in lettersGuessed:
            listi.remove(letter)
    
    # Turn back into string
    final = ''
    for i in listi:
        final += i
    return final

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
    # FILL IN YOUR CODE HERE...
    # Start of the game
    print('Welcome to the game, Hangman!')
    total_let = len(secretWord)
    print('I am thinking of a word that is',total_let,'letters long.')
    guesses_left = 8
    import string
    availableLetters = string.ascii_lowercase
    lettersGuessed = []
    repeatletter = []
    
    # Start of the loop
    while guesses_left != 0:
        # Easy part
        print('-------------')
        print('You have',guesses_left,'guesses left.')
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters:',availableLetters)
        letter_in = input('Please guess a letter: ')
        guess = letter_in.lower()
        
        # Make sure to avoid wasting a chance on an invalid letter
        if guess not in availableLetters:
            print('Oops! You\'ve already guessed that letter:',getGuessedWord(secretWord, lettersGuessed))
            repeatletter += guess
        else:  
            lettersGuessed.append(guess)
            
        if guess in secretWord:
            if guess not in repeatletter:
                print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
        else:
            if guess not in repeatletter:
                guesses_left -= 1        
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord,lettersGuessed):
            print('-------------')
            print('Congratulations, you won!')
            break
    if guesses_left == 0:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was',secretWord,'.')
    return


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = 'sea'
hangman(secretWord)