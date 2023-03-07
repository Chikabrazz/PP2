#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
line = input().split()
heads = int(line[0])
legs = int(line[1])

def solve(numheads, numlegs):
    total = numheads * 2
    total2 = numlegs - total
    rabits = total2 / 2
    return rabits 

rabits = int(solve(heads, legs))
chickens = int(heads - rabits)

print(rabits,chickens)
