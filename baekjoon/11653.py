from sys import stdin
n = int(stdin.readline())
prime = []
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for i in range(2,n+1):
    if isPrime:
        prime.append(i);
        
while n > 1:
    for p in prime:
        if n % p == 0:
            print(p)
            n = n / p
            break
    
        
        
