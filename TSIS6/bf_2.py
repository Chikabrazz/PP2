line = input().split()

def count(txt):
    lower_chr = 0
    upper_chr = 0
    for i in txt: 
        for s in i:
            if s.isupper():
                upper_chr += 1
            elif s.islower():
                lower_chr += 1
    
    print("lower_case:", lower_chr)
    print("upper_case:", upper_chr)

count(line) 