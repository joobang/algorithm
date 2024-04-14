from sys import stdin
x, y, w, h = map(int,stdin.readline().split())

min_distance = min(x, y, w - x, h - y)
print(min_distance)