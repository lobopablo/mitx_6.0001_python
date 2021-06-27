cls = lambda: print("\033[2J\033[;H", end='')
cls()

from ps4a import *
from ps4b import *

wordList = loadWords()

# a = compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
# print(a) 

compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
