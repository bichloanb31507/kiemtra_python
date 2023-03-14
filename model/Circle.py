from kiemtra_Loan.model.Shape import Shape
import math

class Circle(Shape):
    
    def __init__(self, x, y, banKinh):
        super().__init__(x, y)
        self.banKinh = banKinh
        
    def chuVi(self):
        return 2 * math.pi * self.banKinh
    
    def dienTich(self):
        return math.pi * self.banKinh * self.banKinh
        