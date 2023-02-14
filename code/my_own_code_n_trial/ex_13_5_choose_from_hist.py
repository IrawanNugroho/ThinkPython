"""
Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in Section 11.1 
and returns a random value from the histogram, chosen with probability in proportion to frequency. 
For example, for this histogram:
>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> print hist
{'a': 2, 'b': 1}
your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
"""
import random
import ex_11_2_histogram

def choose_from_hist(histrogramDict):
    """
    Actually I do not really understand the problem.
    I write this code because I got inspired by the answer key of exercise 13.4
    """
    t = []
    for key, value in histrogramDict.items():
        t.extend([key] * value)
    
    return random.choice(t)

if __name__ == '__main__':
    t = ['a', 'b', 'c', 'a']
    print(t)

    hist = ex_11_2_histogram.histogram(t)
    print(hist)

    print(choose_from_hist(hist))