from sys import stdin

n = int(stdin.readline())

for i in range(1,n+1):
    star = ""
    for j in range(n-i):
        star += " "
    for j in range(i):
        star += "*"
    print(star)
    
