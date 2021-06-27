#%% Script information
# Name: example6.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Script

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Multiple base cases
    if len(aStr)==0:
        return False
    elif len(aStr)==1 and char!=aStr:
        return False
    else:
    # Define your new string
        midletter = aStr[round(len(aStr)/2)-1]
        if char==midletter:
            return True
        elif char<midletter:
            aStr = aStr[0:round(len(aStr)/2)-1]
        elif char>midletter:
            aStr = aStr[round(len(aStr)/2):len(aStr)]
    # Recursive step with your new, shorter string
        return isIn(char,aStr)

print(isIn('a','abcooooxyz'))