from sys import stdin
n,m = map(int,stdin.readline().split())

arr = [i+1 for i in range(n)]

for z in range(m):
    i,j = map(int, stdin.readline().split())
    prefix = arr[:i-1:]
    temp = arr[i-1:j:]
    reverse_temp = temp[::-1]
    sufix = arr[j::]
    arr = prefix + reverse_temp + sufix


print(' '.join(str(e) for e in arr))