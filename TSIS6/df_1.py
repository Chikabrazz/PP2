import os
path = 'C:\Tmp\pp2\lab6'
print("Directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("Files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])
print("Directories and Files:")
print([ name for name in os.listdir(path)])