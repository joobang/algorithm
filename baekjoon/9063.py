from sys import stdin
n = int(stdin.readline())

minx = 10000
maxx = -10000
miny = 10000
maxy = -10000
for i in range(n):
    arr = list(map(int, stdin.readline().split()))
    if arr[0] > maxx:
        maxx = arr[0]
        
    if arr[0] < minx:
        minx = arr[0]
        
    if arr[1] > maxy:
        maxy = arr[1]
        
    if arr[1] < miny:
        miny = arr[1]
        
print((maxx-minx) * (maxy-miny))