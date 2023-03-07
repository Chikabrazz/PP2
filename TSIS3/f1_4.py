#You are given list of numbers separated by spaces. Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.
line = [int(i) for i in input().split()]

def isprime(a):
    if a == 1:
        return False
    for n in range(2,int(a**1/2)+1):
        if a % n == 0:
            return False
    return True

primes = []

for i in line:
    if isprime(i):
        primes.append(i)
    else:
        pass
    
for i in primes:
    print(i, end=" ")
