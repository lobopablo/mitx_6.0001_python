# Clearing console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Actual code
def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    #YOUR CODE HERE
    # Create the dictionary
    import string
    letters = string.ascii_lowercase
    dict = {}
    for idx,val in enumerate(letters):
        dict[val] = idx + 1
    
    # Evaluating the word
    word = word.lower()
    lettersnscores = {}
    # Key = position, Value = Score
    for idx,val in enumerate(word):
        lettersnscores[idx] = dict[val]
    
    # Creating scores
    values = len(lettersnscores)
    scores = []
    for i in range(0,values):
        scores.append(i*lettersnscores[i])
    
    # Sorting
    scores.sort()
    val1 = scores[len(scores)-1]
    val2 = scores[len(scores)-2]
    
    # Calling f
    result = f(val1,val2)
    return result
    

#%% Test cases


def sum(val1,val2):
    suma = val1+val2
    return suma

def multiply(val1,val2):
    result = val1*val2
    return result

word = 'arDe'
print(score(word,sum))
print(score(word,multiply))

