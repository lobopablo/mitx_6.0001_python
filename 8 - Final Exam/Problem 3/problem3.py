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
            
        # a_div =a_int = int(n/6)
        # a_dec = n/6 - a_int
        # b_int = int(n/9)
        # b_dec = n/9 - b_int
        # c_int = int(n/20)
        # c_dec = n/20 - c_int
        # print(a_int, a_dec, b_int, b_dec, c_int, c_dec)
        # Loop P1
        # while abs(guess - n) > 6:    
        #     a += 1
        #     guess = 6*a + 9*b + 20*c
        #     print(guess)    
        # Return statement|
    return answer
    
n = 15
print(McNuggets(n))
