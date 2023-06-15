a=[1,2,5,7]
b=[1,4,8,5]

arr = a+b
n = len(arr)
for i in range(n):
    # 가장 작은 데이터의 인덱스
    min_idx = i
    for j in range(i+1, n):
        # 최솟값 찾기
        if (arr[min_idx] > arr[j]):
            min_idx = j
    # 데이터 간의 자리 변경
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)