from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

print("%d %d"%(min(arr), max(arr)))