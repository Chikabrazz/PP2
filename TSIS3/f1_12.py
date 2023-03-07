line = [int(i) for i in input().split()]
res=[]

def histogram(numbers):
    ans = []
    for j in range(numbers):
        ans.append("*")
    return ans

for i in line:
    res.append(histogram(i))

for i in res:
    for j in i:
        print(j, end="")
    print()
