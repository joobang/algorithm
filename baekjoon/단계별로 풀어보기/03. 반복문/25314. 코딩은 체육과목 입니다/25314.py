n = int(input())

answer = ""
while n:
    answer += "long "
    n -= 4
    if n == 0:
        answer += "int"

print(answer)