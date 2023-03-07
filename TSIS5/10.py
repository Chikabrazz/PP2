import re
txt = str(input())

pat = r'(.+?)([A-Z])'

def to_snake(txt):
    return txt.group(1).lower() + "_" + txt.group(2).lower()

ans = re.sub(pat, to_snake, txt)
print(ans)