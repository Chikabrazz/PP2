import os

def check(path):
    for item in os.listdir(path):
        target = os.path.join(path, item)
        if os.path.isdir(target):
            for i in os.listdir(target):
                print('File name in directory',target, 'is:', i)
        if os.path.isfile(target):
            print('File name in :', os.getcwd(), 'is:', os.path.basename(target))

path = input()
check(path)

#path -> C:\Tmp\pp2\lab6