x = int(input())
y = int(input())

answer = 0
for i in range(3):
    dy = y%10
    print(x*dy)
    answer += x*dy*(10**i)
    y = y // 10

print(answer)