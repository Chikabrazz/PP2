import re
lst = ["Almaty", "atyraU", "AqTobE", "SHymkent"]

def text_match(txt):
    pat = '[A-Z]+[a-z]+$'
    for i in txt:
        if re.search(pat, i):
            print("Matched")
        else:
            print("Not Matched") 

text_match(lst)