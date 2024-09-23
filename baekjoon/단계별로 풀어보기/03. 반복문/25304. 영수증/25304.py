total = int(input())

n = int(input())

cal = 0
for i in range(n):
    p, q = map(int, input().split())
    
    cal += p*q
    
if total == cal:
    print("Yes")
else:
    print("No")