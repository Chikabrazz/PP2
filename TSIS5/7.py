import re
txt = str(input())
ans = ''.join(y.capitalize() for y in txt.split('_'))
print(ans)