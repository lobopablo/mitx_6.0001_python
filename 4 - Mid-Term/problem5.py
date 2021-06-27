# Clearing console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Actual code

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Create the list of values
    values = []
    for i in aDict.keys():
        values.append(aDict[i])
    # Filter the unique values
    unique_values = []
    for i in values:
        copyaux = values[:]
        copyaux.remove(i)
        if i not in copyaux:
            unique_values.append(i)
    # Find the key to the unique values
    unique_keys= []
    for value in unique_values:
        for key in aDict.keys():
            if value == aDict[key]:
                unique_keys.append(key)
    return unique_keys
#%% Test cases

# Test case #1
a = {'jorge':2, 'paula':2, 'agustin':3, 'pepe':4, 'pablo':4}
print(uniqueValues(a))

