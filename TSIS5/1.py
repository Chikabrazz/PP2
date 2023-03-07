import re
lst = ["abb", "a", "bbb", "ababa", "aac", "ab"]

def text_match(txt):
    pat = '^ab*$'
    for i in txt:
        if re.search(pat, i):
            print("Matched")
        else:
            print("Not Matched")
    
text_match(lst)
# ^ -> Starts with
# $ -> Ends with
# * -> Zero or more occurrences