from OOP_video_code import Triangle

class ColorTriangle(Triangle):
    def __init__(self, a, b, color):
        super().__init__(a,b)
        self.color = color

    def __repr__(self):
        return 

    def describe(self):
        msg = super().describe()
        return msg + f' I am {self.color}'

t = ColorTriangle(3,4,'red')
print(t)