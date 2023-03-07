import os

if not os.path.exists('upper_letters.txt'):
    os.mkdir('upper_letters.txt')

for letters in range(65, 91):
    letters = chr(letters)
    with open(letters + '.txt', 'w') as f:
        f.writelines(letters)