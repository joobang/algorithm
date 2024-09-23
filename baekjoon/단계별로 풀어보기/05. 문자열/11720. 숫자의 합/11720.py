from sys import stdin
n = int(stdin.readline())

str = stdin.readline().rstrip()

answer = 0
for a in str:
    answer += int(a)
    
print(answer)