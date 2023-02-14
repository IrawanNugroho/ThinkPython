"""
Exercise 11.2. Dictionaries have a method called get that takes a key and a default value. 
If the key appears in the dictionary, get returns the corresponding value; 
otherwise it returns the default value. For example:

>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0

Use get to write histogram more concisely. You should be able to eliminate the if statement.
"""
import sys


def histogram(stringInput):
    d = dict()
    for letter in stringInput:
        d[letter] = d.get(letter, 0)
        d[letter] += 1
    return d

def main(name, stringInput):
    if not isinstance(stringInput, str):
        return "Please type string word !"

    print(histogram(stringInput))

if __name__ == '__main__':
    main(*sys.argv)
