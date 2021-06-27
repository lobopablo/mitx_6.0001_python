# Clearing console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Actual code

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Make a copy
    finalList = aList[:]
    for i in aList:
        if len(i)>=4:
            finalList.remove(i)
    return finalList
    
#%% Test cases

# Test case #1
aList = ['apple','cat','dog','banana']
print(lessThan4(aList))
aList = []
print(lessThan4(aList))
