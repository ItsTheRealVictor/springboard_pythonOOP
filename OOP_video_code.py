from random import randint

class Triangle:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def getHyp(self):
        return (self.a**2 + self.b**2) ** .5

    def getArea(self):
        return (self.a * self.b) / 2

    @classmethod
    def randomTri(cls):
        return cls(randint(1,20), randint(1,20))

    def describe(self):
        return f'I am a triangle with sides {self.a} {self.b}'