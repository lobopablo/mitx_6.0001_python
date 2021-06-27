#%% Script information
# Name: script1.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
# cls = lambda: print("\033[2J\033[;H", end='')
# cls()
#%%
low = 0
high = 100
guess = round((low+high)/2)
print('Please think of a number between 0 and 100!')
info = 'l'

while info != 'c':
    strtest = 'Is your secret number ' + str(guess) + '?'
    print(strtest)    
    info = input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly. ')
    if info == 'h':
        high = guess
        guess = int((low+high)/2)
    elif info == 'l':
        low = guess
        guess = int((low+high)/2)
    elif info == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
        
print('Game over. Your secret number was: ' + str(guess))    