# Clearing console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Actual code

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(8))