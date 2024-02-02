from sys import stdin

while True:
    N = int(stdin.readline())
    if N == -1:
        break
    else:
        divisorList = []
        for i in range(1, N):
            if N % i == 0:
                divisorList.append(i)
        divisorSum = sum(divisorList)
        divisorList = [str(item) for item in divisorList]
        if divisorSum == N:
            print(str(N) + " = " + " + ".join(divisorList))
        else:
            print(f"{N} is NOT perfect.")
