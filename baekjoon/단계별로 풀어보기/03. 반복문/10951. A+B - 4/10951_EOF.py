from sys import stdin

data = []
try:
    while True:
        line = stdin.readline().rstrip()
        if not line:
            break
        a,b = map(int, line.split())
        data.append(a+b)
except EOFError:
    pass

for a in data:
    print(a)