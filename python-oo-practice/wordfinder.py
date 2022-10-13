"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    def __init__(self, file):
        self.file = file
        with open(self.file) as f:
            self.contents = f.readlines()
        

    def read_file(self):
        return ([word.strip() for word in self.contents])

    def get_random(self, num):
        pass

words = WordFinder('python-oo-practice\words.txt')
print(words.read_file())
