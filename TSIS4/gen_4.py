n = input().split()
x = int(n[0])
y = int(n[1])

def squares(a,b) :
    for i in range(a,b+1):
        yield i*i

mygenerator = squares(x,y)

for i in mygenerator:
    print(i)
    