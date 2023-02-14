"""
Exercise 17.7. 
This exercise is a cautionary tale about one of the most common, and difficult to find, errors in Python. 
Write a definition for a class named Kangaroo with the following methods: 

1. An __init__ method that initializes an attribute named pouch_contents to an empty list.
2. A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.
3. A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch.

Test your code by creating two Kangaroo objects, assigning them to variables named kanga and roo, 
and then adding roo to the contents of kanga’s pouch.

Download http: // thinkpython. com/ code/ BadKangaroo. py . 
It contains a solution to the previous problem with one big, nasty bug. Find and fix the bug.
If you get stuck, you can download http://thinkpython.com/code/GoodKangaroo.py, 
which explains the problem and demonstrates a solution.
"""

class Kangaroo(object):
    """
    represents a kangaroo
    attribute : pouch_contents
    """
    
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, anyObject):
        """
        Put any type of object into pouch_contents
        """
        self.pouch_contents.append(anyObject)
    
    def __str__(self):
        """
        returns a string representation of the Kangaroo object and the contents of the pouch.
        """
        return str(self.pouch_contents)


def main():
    kanga = Kangaroo()
    roo = Kangaroo()
    roo.put_in_pouch('salt')

    kanga.put_in_pouch(roo)
    kanga.put_in_pouch('sugar')
    kanga.put_in_pouch(['blackpapper', 'onion'])
    print(kanga)
    print(roo)

if __name__ == '__main__':
    main()