"""Word Finder: finds random words from a dictionary."""
from random import randint, choice

class WordFinder:
    '''
        # I'm not a python expert but I think the accepted best practice is to use a context manager for opening files. 
        The solution code uses open() but doesn't close the file, isn't that dangerous? 
    '''


    def __init__(self, file):
        self.file = file
        with open(self.file) as f:
            self.contents = f.readlines()
        

    def read_file(self):
        return ([word.strip() for word in self.contents])

    def get_random(self):
        return choice(self.contents)

words = WordFinder('python-oo-practice\words.txt')
print(words.get_random())
print(words.get_random())
print(words.get_random())
print(words.get_random())
print(words.get_random())