from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

def isPrimeNum(n):
    for i in range(2, n):
        print(n, i)
        if n % i == 0:
            return False
        
    return True

result = 0
for x in arr:
    print(x > 1 and isPrimeNum(x))
    if x > 1 and isPrimeNum(x):
        result += 1

print(result)

