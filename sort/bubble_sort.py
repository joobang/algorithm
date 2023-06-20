def bubble_sort(arr):
    n = len(arr)  # 리스트의 길이를 n에 할당

    # 바깥쪽 루프는 리스트 전체를 돌게 됩니다.
    # i는 비교해야 할 리스트 내의 마지막 인덱스를 나타냅니다.
    for i in range(n-1, 0, -1):  # n-1부터 1까지 역순으로 이동
        # 안쪽 루프는 인접한 요소를 비교하고 교환(필요한 경우)합니다.
        for j in range(i):  
            # 현재의 요소가 다음 요소보다 크다면 위치를 교환합니다.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap
    return arr  # 정렐된 리스트를 반환

# 정렬해야 할 리스트
arr = [64, 34, 25, 12, 22, 11, 90]
# 버블정렬 함수를 호출하고 결과를 출력
print(bubble_sort(arr))
