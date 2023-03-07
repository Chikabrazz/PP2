txt = ("banana", "apple", "orange")
print(type(txt))
def check(txt):
    if type(txt) is tuple:
        print("True")
    else:
        print("False")

check(txt)