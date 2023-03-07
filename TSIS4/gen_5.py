n = int(input())

def reverse(a) :
    while a > -1:
        yield a
        a -= 1

mygenerator = reverse(n)

for i in mygenerator:
    print(i)