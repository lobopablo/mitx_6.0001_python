#%% Script information
# Name: problem7.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Code

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        # Nothing to add here?
        self.Lkeys = []
        self.Lvals = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k not in self.Lkeys:                
            self.Lkeys.append(k)
            self.Lvals.append(v)
        else: 
            # Find the index
            for num,key in enumerate(self.Lkeys):
                if key == k:
                    index = num
            self.Lvals[index] = v
        
    def getval(self, k):
        """ k, immutable object  """
        if k not in self.Lkeys:
            raise KeyError
        else:
            for num,key in enumerate(self.Lkeys):
                if key == k:
                    index = num
            return self.Lvals[index]
        
    def delete(self, k):
        """ k, immutable object """  
        # Check whether k is actually anything
        if k not in self.Lkeys:
            raise KeyError
        else:           
            for num,key in enumerate(self.Lkeys):
                if key == k:
                    index = num
            # Delete values from lists
            self.Lkeys.pop(index)
            self.Lvals.pop(index)

#%% Testing dictionaries

# Test #1
# md = myDict()
# md.assign(1,2)
# print(md.getval(1))
# md.delete(1)

# Test #2
# print('Test: delete 2')
# d1 = myDict()
# d1.assign(1,2)
# d1.delete(3)
# #only looking for a KeyError

# Test #3
# print('Test: getval 1')
# d1 = myDict()
# d1.assign(1,2)
# d1.assign(3,4)
# d1.assign(5,6)
# print(d1.getval(3))

# Test #4
# print('Test: getval 3')
# d1 = myDict()
# d1.assign(1,2)
# d1.assign(3,4)
# print(d1.getval(4))
# #only looking for a KeyError

# Test #5
# d1 = myDict()
# print(d1.getval(3))

# # Test #6
# d1 = myDict()
# d1.assign(10,2)
# print(d1.getval(10))
# d1.assign(3,3)
# print(d1.getval(3))
# print(d1.getval(10))
# d1.assign(4,2)
# print(d1.getval(4))
# d1.assign(3,6)
# print(d1.getval(3))
# print(d1.getval(10))
# print(d1.getval(3))
# print(d1.getval(4))
# d1.delete(3)
# d1.delete(10)
# print(d1.getval(4))

# Test #7
d1 = myDict()
d1.assign(1,2)
d1.assign(3,4)
d1.assign(3,5)
print(d1.getval(3))
        
