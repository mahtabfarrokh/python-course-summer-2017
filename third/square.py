from shape import Shape

class Square (Shape):
    counter = 0
    def __init__(self , c1 , c2 , c3 , c4 , color):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.name = self.findName()
        Square.counter += 1
        super().__init__(self.name , color , 4)
    def findName (self):
        pass

