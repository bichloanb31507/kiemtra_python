import random
from model.Rect import Rect
from model.Triangle import Triangle
from model.Circle import Circle
from shapely.geometry import Polygon, Point
from shapely.ops import unary_union

class FileIO:

    def checkedTriangle(self, a, b, c):
        if (a + b > c and a + c > b and b + c > a):
            return True
        else:
            return False

    def readFile(self, filePath, qty):
        shapes = ["Rect", "Circle", "Triangle"]
        with open(filePath, "w") as f:
            for i in range(qty):
                shape = random.choice(shapes)
                if shape == "Rect":
                    cRong = random.randint(1, 100)
                    cDai = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    f.write("#Rect\n")
                    f.write(f"{cRong} {cDai}\n")
                    f.write(f"{x} {y}\n")
                elif shape == "Circle":
                    bKinh = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    f.write("#Circle\n")
                    f.write(f"{bKinh}\n")
                    f.write(f"{x} {y}\n")
                else:
                    a = random.randint(1, 100)
                    b = random.randint(1, 100)
                    c = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    checked = self.checkedTriangle(a, b, c)
                    if checked == True:
                        f.write("#Triangle\n")
                        f.write(f"{a} {b} {c}\n")
                        f.write(f"{x} {y}\n")
                    else:
                        print("Error!!!")
        
             
    def writeFile(self, filePath):
        shapes = []
        with open(filePath, 'r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                if line == '#Circle':
                    bKinh = float(f.readline().strip())
                    x, y = map(int, f.readline().strip().split())
                    circle = Circle(x, y, bKinh)
                    shapes.append(circle)
                elif line == '#Rect':
                    cRong, cDai = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    rect = Rect(x, y, cRong, cDai)
                    shapes.append(rect)
                elif line == '#Triangle':
                    a, b, c = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    triangle = Triangle(x, y, a, b, c)
                    shapes.append(triangle)
        return shapes
        
    def findLargestShapes(self, shapes):
        maxPerimeterShape = None
        maxAreaShape = None
        for shape in shapes:
            if maxPerimeterShape is None or shape.chuVi() > maxPerimeterShape.chuVi():
                maxPerimeterShape = shape
            if maxAreaShape is None or shape.dienTich() > maxAreaShape.dienTich():
                maxAreaShape = shape
        newShapes = [maxPerimeterShape, maxAreaShape]
        return newShapes;
      
    def unaryUnion(self, filePath): 
        shapes = []
        with open(filePath, 'r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                if line == '#Circle':
                    bKinh = float(f.readline().strip())
                    x, y = map(int, f.readline().strip().split())
                    circle = Point(x, y).buffer(bKinh)
                    shapes.append(circle)
                elif line == '#Rect':
                    cRong, cDai = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    rect = Polygon([(x, y), (x + cRong, y), (x + cRong, y + cDai), (x, y + cDai)])
                    shapes.append(rect)
                elif line == '#Triangle':
                    a, b, c = map(float, f.readline().strip().split())
                    x, y = map(int, f.readline().strip().split())
                    triangle = Polygon([(x, y), (x + b, y), (x + c, y + a), (x, y)])
                    shapes.append(triangle)
        newShapes = unary_union(shapes)
        return ', '.join([f'{shape:.3f}' for shape in newShapes.bounds])
        