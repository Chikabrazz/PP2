import re
lst = ["abbcac", "abababab", "cbdacb"]

def text_match(txt):
    pat = 'a.+b$'
    for i in txt:
        if re.search(pat, i):
            print("Matched")
        else:
            print("Not Matched") 

text_match(lst)

# . -> Any character (except newline character)
# $ -> Ends with