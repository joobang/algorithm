from sys import stdin

answer = set()
for i in range(10):
    n = int(stdin.readline())
    answer.add(n%42)

print(len(answer))