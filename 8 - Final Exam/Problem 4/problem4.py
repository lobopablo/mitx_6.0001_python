#%% Script information
# Name: problem4.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Code
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    tupleout = False
    cond1 = False
    cond2 = False    
    # Check condition 1: length
    if len(L1)!=len(L2):
        cond1 = False
    # Check condition 2: permutation
    elif len(L1) == 0 and len(L2) == 0:
        tupleout = (None, None, None)
    else:
        cond1 = True
        # Create Dictionary #1
        dict_L1 = {}
        for item in L1:
            if item in dict_L1:
                dict_L1[item] += 1
            else:
                dict_L1[item] = 1
        # Create Dictionary #2
        dict_L2 = {}
        for item in L2:
            if item in dict_L2:
                dict_L2[item] += 1
            else:
                dict_L2[item] = 1
        if dict_L1 == dict_L2:
            cond2 = True    
    if cond1==True and cond2==True:
        maxkey = max(dict_L1, key=dict_L1.get)
        maxval = dict_L1[maxkey]
        typemax = type(maxkey)
        tupleout = (maxkey,maxval,typemax)
    return tupleout

#%% Testing

# True case, 1, 3, int
print('Case #1')
L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))


# False case
print('Case #2')
L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 'b', 1, 1, 'c']
print(is_list_permutation(L1, L2))

# Empty case
print('Case #3')
L1 = []
L2 = []
print(is_list_permutation(L1, L2))