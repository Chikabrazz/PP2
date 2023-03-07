line = [int(i) for i in input().split()]

def has_33(numbers):
    for i in range(2,len(numbers)):
        if numbers[i-1] == 3 and numbers[i] == 3:
            return True
    return False

if has_33(line):
    print("True")
else:
    print("False")