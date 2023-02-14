"""
Exercise 12.4. More anagrams!

1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.

Here is an example of what the output might look like:
     ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
     ['retainers', 'ternaries']
     ['generating', 'greatening']
     ['resmelts', 'smelters', 'termless']

Hint: you might want to build a dictionary that maps from a set of letters to a list of words 
that can be spelled with those letters. 
The question is, how can you represent the set of letters in a way that can be used as a key?
"""

def sorted_string_key(word):
    """
    This function is key, when we are talking about anagram
    What is the use of tuple for this exercise, then? 
    """
    key = list(word)
    key.sort()
    delimiter = ''
    key = delimiter.join(key)
    
    return key

def raw_anagram_like_word_dict(filename):
    fin = open(filename)
    wordDict = dict()
    for line in fin:
        word = line.strip().lower()
        index = sorted_string_key(word)
        wordDict.setdefault(index, [])
        wordDict[index].append(word)
        
        
    return wordDict

def anagram_dict(wordDict):
    anagramDict = dict()
    
    for key, value in wordDict.items():
        if len(value) > 1:
            anagramDict[key] = value
    
    return anagramDict

if __name__ == '__main__':
    wordDict = raw_anagram_like_word_dict('words.txt')
    myAnagramDict = anagram_dict(wordDict)

    for key, value in myAnagramDict.items():
        print(key, ': ', value)