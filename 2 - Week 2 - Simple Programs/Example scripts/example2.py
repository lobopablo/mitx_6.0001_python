#%% Script information
# Name: script2.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
# cls = lambda: print("\033[2J\033[;H", end='')
# cls()
#%%
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    if exp == 0:
        result = 1
    elif exp == 1:
        result = base
    else:
        while exp>1:
            result *= base
            exp -= 1
    return result

test1 = iterPower(4,3)