with open('ex.txt', 'w') as f:
    while True:
        s = input()
        if s == '0':
            break
        f.writelines([s, '\n'])