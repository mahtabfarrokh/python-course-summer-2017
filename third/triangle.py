from shape import Shape

class Triangle (Shape):
    tcounter = 0
    def __init__(self , c1 , c2 , c3 , color):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        Triangle.tcounter += 1
        super().__init__("triangle " + str(Triangle.tcounter) , color , 3 )

