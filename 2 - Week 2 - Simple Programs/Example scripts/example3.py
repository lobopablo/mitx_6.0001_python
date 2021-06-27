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
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Base case
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*recurPower(base,exp-1)

