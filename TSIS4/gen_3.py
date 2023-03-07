n = int(input())

mygenerator = (i for i in range(0, n+1) if (i % 3 == 0) and (i % 4 == 0))

for i in mygenerator:
    print(i)