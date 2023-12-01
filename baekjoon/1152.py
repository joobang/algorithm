from sys import stdin
str_list = stdin.readline().rstrip().split()
answer = 0
for i in str_list:
    answer += 1
    
print(answer)