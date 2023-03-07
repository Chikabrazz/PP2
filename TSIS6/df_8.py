import os
path = input()

if os.path.exists(path):
    os.remove(path)
else:
    print("Not Exist")

#path -> C:\Tmp\pp2\lab6\file_to_remove.txt