import math

def area(n,a):
    x = math.pi
    return int(n * a*a * int(1 / math.atan(x/n)) / 4)
    
side = int(input("number of sides: "))
length = int(input("the length of a side: "))

print("The area of the polygon is: " + str(area(side,length)))