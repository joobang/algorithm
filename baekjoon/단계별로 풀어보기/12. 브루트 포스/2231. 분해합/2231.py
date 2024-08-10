from sys import stdin
n = int(stdin.readline())
def findNum(a):
    for b in range(1, a + 1):
        digit_sum = sum(int(digit) for digit in str(b))
        if b + digit_sum == a:
            return b
    return 0

print(findNum(n))