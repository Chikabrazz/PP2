class Square:
    def __init__(self, length):
        self.length  = length

    def area (self):
        self.length * self.length == 0

class Shape(Square):
    def __init__(self, length):
        self.length  = length
    
    def area(self) :
        return self.length * self.length 
    
class Rectangle(Shape):
    def ___inti___(self, width):
        self.width = width
    def area(self):
        return self.length * self.width
    

a = int(input())
p1 = Shape(a)

n = int(input())
p2 = Rectangle(n)
print(p2.area())