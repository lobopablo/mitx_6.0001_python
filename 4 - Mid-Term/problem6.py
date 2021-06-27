# Clearing console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Actual code
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Base case    
    rightd = N % 10
    leftd = N // 10
    if rightd == N:
        return rightd
    # Recursive step
    else:
        return rightd + sumDigits(leftd)
   
    
    
#%% Test cases
N = 127
print(sumDigits(N)) # 10
N = 1385
print(sumDigits(N)) # 17
N = 8
print(sumDigits(N)) # 8


