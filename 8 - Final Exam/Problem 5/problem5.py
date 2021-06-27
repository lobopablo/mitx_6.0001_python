#%% Script information
# Name: problem5.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Code
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    Lout = []
    Laux = []
    # Create List with values
    for i in aDict.values():
        Laux.append(i)
    # Create Dict with frequency of values
    dict_aux = {}
    for item in Laux:
        if item in dict_aux:
            dict_aux[item] += 1
        else:
            dict_aux[item] = 1
    # Create List with unique values
    L_values = []
    for item in dict_aux.keys():
        if dict_aux[item]==1:
            L_values.append(item)
    # Create List with keys of unique values
    for item in aDict.keys():
        for value in L_values:
            if aDict[item]==value:
                Lout.append(item)   
    # Sort list
    Lout = sorted(Lout)
    return Lout

#%% Testing

# Case #1
print('Case #1')
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}   
print(uniqueValues(aDict))

# Case #2
print('Case #2')
aDict = {1: 1, 2: 1, 3: 1}
print(uniqueValues(aDict))
