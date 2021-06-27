#%% Script information
# Name: example1.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Code
import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
                
        lows = string.ascii_lowercase
        uppers = string.ascii_uppercase
        
        # Create Dictionary Lows
        dict_low = {}
        for (letter,idx) in zip(lows,range(0,len(lows))):
            dict_low[letter] = idx
        # Modify Dictionary Lows
        for orig_let in dict_low.keys():
            sum_val = dict_low[orig_let] + shift
            if sum_val <= 25:
                dict_low[orig_let] = lows[sum_val]
            else:
                dict_low[orig_let] = lows[sum_val - 26]
        
        # Create Dictionary Uppers
        dict_upp = {}
        for (letter,idx) in zip(uppers,range(0,len(lows))):
            dict_upp[letter] = idx
        # Modify Dictionary Uppers
        for orig_let in dict_upp.keys():
            sum_val = dict_upp[orig_let] + shift
            if sum_val <= 25:
                dict_upp[orig_let] = uppers[sum_val]
            else:
                dict_upp[orig_let] = uppers[sum_val - 26]    
        
        # Merge
        out_dict = dict_low.copy()
        out_dict.update(dict_upp)
        
        return out_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        strout = ''
        strin = self.get_message_text()
        strin = str(strin)
        dict_out = self.build_shift_dict(shift)
        for i in strin:
            if i.isalpha():
                strout += dict_out[i]
            else:
                strout += i  
        return strout
            
shift = 2
test1 = Message('hey how are you!')
print(test1.apply_shift(shift))

