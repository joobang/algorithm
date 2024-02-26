from sys import stdin

N, K = map(int , stdin.readline().split())
cnt = 0
result = 0
for x in range(1,N+1):
    if N % x == 0:
        cnt += 1;
        if cnt == K:
            result = x
            break

print(result)

