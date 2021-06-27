#%% Script information
# Name: problem3v2.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()

# ord('a') - 97
# chr(97) - 'a'
# range(97,123), from a to z
#%%
s = 'zaabbbceefhhhiaelabcdefghijklmnop'
vec = range(1,len(s))

count = 0
indexstart = 0
lenlong = 0

for letter in vec:
    num_ant = ord(s[letter-1])
    num = ord(s[letter])
    if num >= num_ant:
        count += 1
        print('Letras seguidas alfabeticamente: ', str(count))
        if count == 1:
            indexstart = letter - 1
            print('Buena racha comenzo en: ',str(indexstart))
    else:
        indexstop = letter
        print('Frenamos en letra # ',str(indexstop))
        if indexstop - indexstart > lenlong:
            longest = s[indexstart:indexstop]
            lenlong = len(longest)
            print(longest)
        count = 0

        



