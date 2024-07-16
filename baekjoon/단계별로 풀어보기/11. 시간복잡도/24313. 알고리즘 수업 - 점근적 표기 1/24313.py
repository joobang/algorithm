from sys import stdin
a1, a0 = map(int,stdin.readline().split())
c = int(stdin.readline())
n = int(stdin.readline())

result = True
for i in range(n, 10001):
    fn = a1*i + a0
    if fn <= c*i:
        pass
    else:
        result = False
        break;

if result and c >= a1:
    print(1)
else:
    print(0)