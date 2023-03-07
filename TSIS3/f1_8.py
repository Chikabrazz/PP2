line = [int(i) for i in input().split()]

def spy_game(numbers):
    for i in range(2, len(numbers)):
        if numbers[i-1] == 0 and numbers[i] == 0 and numbers[i+1] == 7:
            return True
    return False

if spy_game(line):
    print("True")
else:
    print("False")
    