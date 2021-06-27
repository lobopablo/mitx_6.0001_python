#%% Script information
# Name: example5.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%%
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    guess = min(a,b)
    while guess > 1:
        if a%guess==0 and b%guess==0:
            result = guess
            break
        else:
            guess -= 1
    return result
            


print(gcdIter(9,12))