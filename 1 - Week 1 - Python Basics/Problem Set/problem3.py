#%% Script information
# Name: problem3.py
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
mat = [0] * len(s)

# Processing
for letter in vec:
    num_ant = ord(s[letter-1])
    num = ord(s[letter])
    if num >= num_ant:
        mat[letter] = mat[letter-1] + 1

# Getting string
maxval = max(mat) # This value is length -1 of final str
k = mat.index(maxval)
longest = s[k-maxval:k+1]

print('Longest substring in alphabetical order is:',longest)



