from sys import stdin
n,m = map(int,stdin.readline().split())

arr = [0 for _ in range(n)]

def putBall(i,j,k,arr):
    for z in range(i-1,j):
        arr[z] = k
        
for z in range(m):
    i,j,k = map(int,stdin.readline().split())
    putBall(i,j,k,arr)

print(' '.join(str(e) for e in arr))