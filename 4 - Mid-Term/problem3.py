# Clearing console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Actual code

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Create the dictionary
    dict = {}
    # Eliminate floats
    num = int(num)
    # Find the minimum difference
    for i in range(0,num):
        dict[i] = abs(base**i - num)    
    mindiff = min(dict.values())
    # Find the minimum exponent that creates that value
    for i in range(0,num):
        if abs(base**i - num) == mindiff:
            answer = i
            break
    return answer

#%% Test cases

# Test case #1
print(closest_power(3,12)) # Should return 2
print(closest_power(4,12)) # Should return 2
print(closest_power(4,1)) # Should return 0
print(closest_power(3,26)) # Should return 3
print(closest_power(2,12)) # Should return 3
print(closest_power(10, 550.0)) # Should return 2


