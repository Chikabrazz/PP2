class Square:
    def __init__(self, length):
        self.length  = length

    def area (self):
        self.length * self.length == 0

class Shape(Square):
    def __init__(self, length):
        self.length  = length
    
    def area (self) :
        return self.length * self.length 

a = int(input())
p1 = Shape(a)
print(p1.area())