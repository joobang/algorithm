from sys import stdin

N, M = map(int , stdin.readline().split())

num_list = list(map(int, stdin.readline().split()))
sumValue = 300000
# result = []

for i in range(N):
    #print('first : ' + str(i))
    for j in range(i + 1, N):
        #print('second : ' + str(j))
        for k in range(j + 1, N):
            #print('third : ' + str(k))
            #print(num_list[i] + num_list[j] + num_list[k])
            subSum = num_list[i] + num_list[j] + num_list[k]
            if abs(M - subSum) < abs(M - sumValue) and subSum <= M:
                sumValue = subSum

print(sumValue)
   
def getCombination(arr, M, start, currentList, bestSum):
    if len(currentList) == 3:
        currentSum = sum(currentList)
        if currentSum <= M and abs(M - currentSum) < abs(M - bestSum):
            bestSum = currentSum
        return bestSum

    for i in range(start, len(arr)):
        currentList.append(arr[i])
        bestSum = getCombination(arr, M, i + 1, currentList, bestSum)
        currentList.pop()

    return bestSum

# 초기 값 설정
bestSum = 300000
currentList = []
# 재귀 함수 호출
bestSum = getCombination(num_list, M, 0, currentList, bestSum)

print(bestSum)