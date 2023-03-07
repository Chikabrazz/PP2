import math

radius = int(input())

def volume(radius):
    return 4/3* math.pi * int(radius)*int(radius)*int(radius)

print(volume(radius))