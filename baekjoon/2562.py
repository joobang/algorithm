from sys import stdin

max = 0
max_i = 1
for i in range(1,10):
    x = int(stdin.readline())
    if x > max:
        max_i = i
        max = x
    
print(max)
print(max_i)