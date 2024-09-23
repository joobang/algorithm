from sys import stdin

arr = []
answer = []
for i in range(28):
    n = int(stdin.readline())
    arr.append(n)

for i in range(30):
    if i+1 not in arr:
        answer.append(i+1)        

answer.sort()
print(answer)
for i in answer:
    print(i)