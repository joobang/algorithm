M = int(input())
N = int(input())

min = N
primeArr = []
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for x in range(M, N+1):
    if isPrime(x) and x > 1:
        primeArr.append(x)
        if min > x:
            min = x

if len(primeArr) > 0:
    print(sum(primeArr))
    print(min)
else:
    print(-1)