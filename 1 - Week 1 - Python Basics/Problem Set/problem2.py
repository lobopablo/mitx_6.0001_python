#%% Script information
# Name: problem2.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()# -*- coding: utf-8 -*-
#
#%% Actual problem
# s = 'lowercase str1ng, w some sp3cial charact3rs.  .a' # Answer - 11
s = 'xbobobbooboboboobbbobbobobobbeuobobobob'

napps = 0
vec = range(0,len(s)-2)

for start in vec:
    slicestr = s[start:start+3]
    if slicestr == 'bob':
        napps += 1
    

print('Number of times bob occurs is: ' + str(napps))

            


