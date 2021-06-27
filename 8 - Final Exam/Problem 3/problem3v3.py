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
    answer = False 
    # Initial Guess
    if n < 6:
        answer = False
    else:
        # Easy case
        a_ez = n/6
        b_ez = n/9
        c_ez = n/20
        if a_ez.is_integer() or b_ez.is_integer() or c_ez.is_integer():
            answer = True
        # Not so easy cases
        else:
            guesslist = []
            lista = []
            listb = []
            listc = []
            # Loop a
            for a in range(0,int(a_ez)+1):
                guess = a*6
                lista.append(guess)
            # Loop b
            for b in range(0,int(b_ez)+1):
                guess = b*9
                listb.append(guess)
            # Loop c
            for c in range(0,int(c_ez)+1):
                guess = c*20
                listc.append(guess)
            # Total list
            for i in lista:
                for j in listb:
                    for k in listc:
                        guesslist.append(i+j+k)           
            # Sort and eliminate duplicates
            guesslist = list(dict.fromkeys(guesslist))
            guesslist = sorted(guesslist)
            # Check if number is in there
            if n in guesslist:
                answer = True                
    return answer
    
n = 
print(McNuggets(n))
