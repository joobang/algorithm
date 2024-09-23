from sys import stdin
n = stdin.readline().rstrip()

answer = ""
alpa = "abcdefghijklmnopqrstuvwxyz"
for a in alpa:
    index = n.find(a)
    if len(answer) == 0:
        answer += str(index)
    else:
        answer = answer + " " + str(index)

print(answer)    