from sys import stdin
len_list = list(map(int, stdin.readline().split()))
max_len = max(len_list)

if sum(len_list) - (2*max_len) > 0:
    print(sum(len_list))
else:
    print(2*(sum(len_list) - max_len) - 1)