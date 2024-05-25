from sys import stdin
n = int(stdin.readline())

# def eachSum(n):
#     list_n = list(range(1,n+1))
#     return sum(list_n)

def eachSum(n):
    return n * (n + 1) // 2

cnt = 0
for i in range(n - 2, 0, -1):
    cnt += eachSum(i)
    
print(cnt)
print(3)