from sys import stdin
n,m = map(int, stdin.readline().split())

arr = [i+1 for i in range(n)]

for z in range(m):
    i,j = map(int, stdin.readline().split())
    temp = arr[j-1]
    arr[j-1] = arr[i-1]
    arr[i-1] = temp

print(' '.join(str(e) for e in arr))
