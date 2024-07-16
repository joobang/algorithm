from sys import stdin
n = int(stdin.readline())

for i in range(n):
    str = stdin.readline().rstrip()
    print(str[0]+ str[len(str)-1])