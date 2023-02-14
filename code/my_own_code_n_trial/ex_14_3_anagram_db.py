"""
Exercise 14.3. If you download my solution to Exercise 12.4 from http: // thinkpython. com/ code/ anagram_ sets. py , 
you’ll see that it creates a dictionary that maps from a sorted string of letters to the list of words 
that can be spelled with those letters. 

For example, 'opst' maps to the list ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions: 

store_anagrams should store the anagram dictionary in a “shelf;” 

read_anagrams should look up a word and return a list of its anagrams. 

Solution: http: // thinkpython. com/ code/ anagram_ db. py
"""
import ex_12_4_more_anagrams
import dbm
import pickle

def store_anagrams(anagramDictionary):
    db = dbm.open('ex_14_3_anagrams.db', 'c')
    for key, value in anagramDictionary.items():
        
        if isinstance(key, str):
            print(key, value)
            db[key] = value
        else:
            tmp = pickle.dumbs(key)
            db[tmp] = value    
    db.close()
    
    return "anagrams are stored!"

if __name__ == '__main__':
    wordDict = ex_12_4_more_anagrams.raw_anagram_like_word_dict('words.txt')
    myAnagramDict = ex_12_4_more_anagrams.anagram_dict(wordDict)
    print(store_anagrams(myAnagramDict))