#%% Script information
# Name: problem3.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Code
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    answer = False #################### BORRARRRRRR########
    # Initial Guess
    if n < 6:
        answer = False
    else:
        # Easy case
        a_ez = n/6
        b_ez = n/9
        c_ez = n/20
        if a_ez.is_integer() or b_ez.is_integer() or c_ez.is_integer():
            print('ez case!')
            answer = True
        else:
            guesslist = []
            # Not so easy cases
            # Loop a
            for a in range(0,int(a_ez)+1):
                guess = a*6
                guesslist.append(guess)
            # Loop b
            for b in range(0,int(b_ez)+1):
                guess = b*9
                guesslist.append(guess)
            # Loop c
            for c in range(0,int(c_ez)+1):
                guess = c*20
                guesslist.append(guess)
            guesslist = list(dict.fromkeys(guesslist))
            # Somewhat hard cases
            
            guesslist = sorted(guesslist)
            print(guesslist)
    return answer
    
n = 23
print(McNuggets(n))
