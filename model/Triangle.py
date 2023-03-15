import math
from model.Shape import Shape

class Triangle(Shape):
    
    def __init__(self, x, y, a, b, c):
        Shape.__init__(x, y)
        self.a = a
        self.b = b
        self.c = c
        
    def chuVi(self):
        return self.a + self.b + self.c
    
    def dienTich(self):
        x = self.chuVi() / 2
        return math.sqrt(x * (x - self.a) * (x - self.b) * (x - self.c))