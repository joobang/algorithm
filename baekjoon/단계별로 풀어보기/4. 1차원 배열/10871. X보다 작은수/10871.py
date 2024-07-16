from sys import stdin
n, x = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
lows = []
for i in arr:
    if i < x:
        lows.append(i)
        
print(' '.join(str(e) for e in lows))