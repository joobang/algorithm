from sys import stdin

while True:
    answer_list = list(map(int, stdin.readline().split()))
    answer_set = set(answer_list)
    if sum(answer_set) == 0:
        break;
    
    max_val = max(answer_list)
    if len(answer_set) == 1:
        print('Equilateral')
    else:
        if sum(answer_list) - (2*max_val) <= 0:
            print('Invalid')
        else:
            if len(answer_set) == 2:
                print('Isosceles')
            elif len(answer_set) == 3:
                print('Scalene')
    
    
            
