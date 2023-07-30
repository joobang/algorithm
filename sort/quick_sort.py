def quicksort(arr):
    # 배열의 크기가 1 이하이면 정렬할 필요가 없으므로 해당 배열을 반환한다.
    if len(arr) <= 1:
        return arr
    
    # 배열의 가운데 값을 pivot으로 지정한다.
    pivot = arr[len(arr) // 2]
    
    # pivot을 기준으로 작은 값은 left 배열, 큰 값은 right 배열, 같은 값은 equal 배열에 담는다.
    left = []
    right = []
    equal = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    
    # left, equal, right 배열을 각각 재귀적으로 정렬한 후 합쳐서 반환한다.
    return quicksort(left) + equal + quicksort(right)