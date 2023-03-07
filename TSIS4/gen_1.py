n = int(input())

mygenerator = (x*x for x in range(1, n+1))

for i in mygenerator:
    print(i)