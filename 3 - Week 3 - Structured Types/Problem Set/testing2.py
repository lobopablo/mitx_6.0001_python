cls = lambda: print("\033[2J\033[;H", end='')
cls()

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

print(getAvailableLetters(['m', 'z', 'g', 'l', 'e', 'd', 'p', 'x']))



