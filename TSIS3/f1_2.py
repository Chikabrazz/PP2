#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def func(f):
    return (5/9) * (f - 32)

n = int(input())
print(func(n))