n = int(input())

mygenerator = (x for x in range(0, n+1, 2))

for i in mygenerator:
    print(i)