import re
lst = ["abb", "ab", "abc", "baa", "abbb"]

def text_match(txt):
    pat = 'ab{2,3}'
    for i in txt:
        if re.search(pat, i):
            print("Matched")
        else:
            print("Not Matched")
        
text_match(lst)
# {} -> Exactly the specified number of occurrences