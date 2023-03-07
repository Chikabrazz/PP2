line = [str(i) for i in input().split()]

def unique(text):
    lst = []
    for i in text:
        if i not in lst:
            lst.append(i)
        else:
            pass
    return lst

for i in unique(line):
    print(i, end=" ")