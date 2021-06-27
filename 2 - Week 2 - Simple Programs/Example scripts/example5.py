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
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case
    guess = min(a,b)
    if b == 0:
        return a
    else:
        if a%guess==0 and b%guess==0:
            return guess
        else:
            return gcdRecur(b, a%b)

print(gcdRecur(9,12))
print(gcdRecur(52, 16))