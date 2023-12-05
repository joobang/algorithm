from sys import stdin
arr = list(map(int, stdin.readline().split()))
chess = [1,1,2,2,2,8]

answer = ""
for i in range(len(chess)):
    if i == 0:
        answer += str(chess[i] - arr[i])
    else:
        answer = answer + " " + str(chess[i] - arr[i])
        
print(answer)

