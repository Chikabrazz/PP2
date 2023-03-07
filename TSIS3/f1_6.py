
text = [str(i) for i in input().split()]
def reversed(text):
    rvs = []
    x = len(text)
    for i in range(x-1,-1,-1):
        rvs.append(text[i])
    return rvs

for i in reversed(text):
    print(i, end=" ")