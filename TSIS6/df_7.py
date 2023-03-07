with open('ex.txt', 'r') as first:
    with open('example.txt', 'w') as second:
        for line in first:
            second.writelines(line)