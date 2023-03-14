
from kiemtra_Loan.model.Shape import Shape

class Triangle(Shape):
    
    def __init__(self, x, y, a, b, c):
        super.__init__(x, y)
        self.a = a
        self.b = b
        self.c = c
        
    def chuVi(self):
        return self.a + self.b + self.c
    
    def dienTich(self):
        c = self.chu