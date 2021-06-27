# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:17:41 2016

@author: WELG
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    val = 0
    for i in aDict:
        lentest = len(aDict[i])
        if lentest>val:
            val = lentest
            text = i
    return text

print(biggest(animals))

    