from sys import stdin

try:
    while True:
        line = stdin.readline().rstrip()
        if not line:
            break
        print(line)
except EOFError:
    pass
