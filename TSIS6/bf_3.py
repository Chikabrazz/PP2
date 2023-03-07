word = str(input())
rword = word[::-1]

def isPalindrome(word, rword):
    if word == rword:
        print("YES")
    else:
        print("NO")
        
isPalindrome(word, rword)   