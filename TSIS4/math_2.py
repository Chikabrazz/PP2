def area(h,f,s):
    return (f+s)/2 * h

h = int(input("Height: "))
f = int(input("Base, first value: "))
s = int(input("Base, second value: "))

print("Area " + str(area(h,f,s)))