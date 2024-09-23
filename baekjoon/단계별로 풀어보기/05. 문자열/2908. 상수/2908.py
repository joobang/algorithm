from sys import stdin
a,b = stdin.readline().rstrip().split()

reverse_a = list(reversed(a))
reverse_b = list(reversed(b))

int_a = int("".join(reverse_a))
int_b = int("".join(reverse_b))

if int_a > int_b:
    print(int_a)
else:
    print(int_b)
