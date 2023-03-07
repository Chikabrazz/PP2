import re
lst = ["zxc_xyz", "abc_DEA", "abc_def", "xzc-cxz"]

def text_match(txt):
    pat = '^[a-z]+_[a-z]+$'
    for i in txt:
        if re.search(pat, i):
            print("Matched")
        else:
            print("Not Matched")

text_match(lst)

# [] -> A set of characters