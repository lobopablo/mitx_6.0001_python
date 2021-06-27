#%% Script information
# Name: problem1.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
# cls = lambda: print("\033[2J\033[;H", end='')
# cls()
#%%
# s = 'lowercase str1ng, w some sp3cial charact3rs.  .a' # Answer - 11
s = 'azcbobobegghakl' # Answer - 5

nvowel = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        nvowel += 1
print('Number of vowels: ' + str(nvowel))
