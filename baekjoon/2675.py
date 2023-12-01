from sys import stdin
n = int(stdin.readline())

answer = []
for i in range(n):
    r_str, p = stdin.readline().rstrip().split()
    r = int(r_str)
    temp = ""
    for x in p:
        for j in range(r):
            temp += x
    
    answer.append(temp)

for x in answer:
    print(x)