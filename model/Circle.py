from model.Shape import Shape
import math

class Circle(Shape):
    
    def __init__(self, x, y, bKinh):
        Shape.__init__(x, y)
        self.bKinh = bKinh
        
    def chuVi(self):
        return 2 * math.pi * self.bKinh
    
    def dienTich(self):
        return math.pi * self.bKinh * self.bKinh
        