from sys import stdin

answer_list = []
for i in range(3):
    n = int(stdin.readline())
    answer_list.append(n)
    
if sum(answer_list) == 180:
    answer = set(answer_list)
    if len(answer) == 3:
        print('Scalene')
    elif len(answer) == 2:
        print('Isosceles')
    else:
        print('Equilateral')
else:
    print('Error')
            
