from sys import stdin

isTrue = True

while isTrue:
    a,b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        isTrue = False
    else:
        print(a+b)
    
