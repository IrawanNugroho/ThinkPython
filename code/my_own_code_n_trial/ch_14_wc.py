def linecount(filename):
    """
    save this function as python file named wc.py
    """
    count = 0
    
    for line in open(filename):
        count += 1
    
    return count

if __name__ == '__main__':
    print(linecount('wc.py'))
else:
    print(__name__)