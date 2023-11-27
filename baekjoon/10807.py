from sys import stdin
n = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))
target = int(stdin.readline())

cnt = 0
for i in arr:
    if i == target:
       cnt += 1
       
print(cnt) 