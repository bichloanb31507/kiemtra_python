from model.Shape import Shape

class Rect(Shape):
    
    def __init__(self, x, y, cRong, cDai):
        Shape.__init__(x, y)
        self.cRong = cRong
        self.cDai = cDai
        
    def chuVi(self):
        return 2 * (self.cRong + self.cDai)
        
    def dienTich(self):
        return self.cRong * self.cDai
        