from sys import stdin
n = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))

max = max(arr)
total = 0
for i in range(n):
    temp = arr[i]/max*100
    total += temp

print(total/n)