import random

class FileIO:

    def __init__(self):
        pass

    def checkedTriangle(self, a, b, c):
        if (a + b > c and b + c > a and a + c > b ):
            return True
        else:
            return False

    def readFile(self, qty):
        shapes = ["Rect", "Circle", "Triangle"]
        with open("D:\input.txt", "w") as file:
            for i in range(qty):
                shape = random.choice(shapes)
                if shape == "Rect":
                    width = random.randint(1, 100)
                    height = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    file.write("#Rect\n")
                    file.write(f"{width} {height}\n")
                    file.write(f"{x} {y}\n")
                elif shape == "Circle":
                    radius = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    file.write("#Circle\n")
                    file.write(f"{radius}\n")
                    file.write(f"{x} {y}\n")
                else:
                    a = random.randint(1, 100)
                    b = random.randint(1, 100)
                    c = random.randint(1, 100)
                    x = random.randint(0, 1000)
                    y = random.randint(0, 1000)
                    check = self.checkedTriangle(a, b, c)
                    if check == True:
                        file.write("#Triangle\n")
                        file.write(f"{a} {b} {c}\n")
                        file.write(f"{x} {y}\n")
                    else:
                        print("triangle - error!!!")
                        
    def writeFile(self, text):
        shapes = []
        lines = text.split('\n')
        for line in lines:
            if line.startswith('#Rect'):
                width, height = map(int, line[6:].split())
                shapes.append(('rect', width, height))
            elif line.startswith('#Circle'):
                radius = int(line[7:])
                shapes.append(('circle', radius))
            elif line.startswith('#Triangle'):
                sides = list(map(int, line[9:].split()))
                x, y = map(int, lines[lines.index(line) + 1].split())
                shapes.append(('triangle', sides, x, y))
        return shapes
