def heapify(arr, n, i):
    """
    주어진 배열을 힙으로 만드는 함수입니다.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Heap Sort 알고리즘을 구현한 함수입니다.
    """
    n = len(arr)

    # 주어진 배열을 힙으로 만듭니다.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 추출한 값을 제외한 나머지 요소들로 다시 힙을 만들고 정렬합니다.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr