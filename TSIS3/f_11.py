word = str(input())

def palindrome(txt):
    new_word = txt[::-1]
    if txt == new_word:
        return True
    else:
        return False
    

if palindrome(word):
    print("YES")
else:
    print("NO")
    