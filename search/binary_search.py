"""
    이진 탐색
    이진 탐색(이분 탐색) 알고리즘은 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법이다.
        
    서로 다른 정수들을 원소로 갖고 있는 정렬되어 있는 리스트가 있다고 가정하자.
    특정 정수값 searchnum이 리스트에 존재하는지 알고싶다.
    만일 searchnum이 리스트에 존재한다면 list[i] = searchnum인 인덱스 i를 반환하고, 그렇지 않다면 -1을 반환한다.

    순차적으로 탐색하는 것보다 훨씬 효율적이다 (리스트가 정렬되어 있을 경우에 대해서만)
    
    - left: 탐색하고자 하는 배열의 왼쪽
    - right: 탐색하고자 하는 배열의 오른쪽
    - middle: (left+right)/2
    
    list[middle]과 searchnum을 비교하여 다음의 세가지 경우 중 하나를 선택한다.

    - searchnum < list[middle] : 다음에 탐색해야할 곳은 list[left] ~ list[middle-1]이다. (right = middle-1로 바꾼다)
    - searchnum = list[middle] : middle을 반환한다.
    - searchnum > list[middle] : 다음에 탐색해야 할 곳은 list[middle+1] ~ list[right]이다. (left = middle+1로 바꾼다)
    
    
    언제까지 반복하는가?

    1. searchnum = list[middle]을 발견하거나
    2. (리스트에 searchnum이 존재하지 않을 경우) left > right 될때 stop!
       (left <= right 이면 계속해서 searchnum과 list[middle]을 비교해주어야 한다.)
       
    시간 복잡도는 O(logN)이다. 
"""
## sorted_list : 정렬된 리스트
## searchnum : 특정 정수. 리스트 안에 존재한다면 인덱스 값을, 존재하지 않는다면 -1을 return한다.

def binary_search(sorted_list, searchnum):
    left = 0
    right = len(sorted_list)-1
    
    while(left <= right):
        ## middle은 left와 right의 중간지점
        middle = (left+right)//2
        
        ## searchnum이 list[middle]보다 작다. right = middle-1
        if searchnum < sorted_list[middle]:
            right = middle - 1
        ## searchnum이 list[middle]보다 크다. left = middle+1
        elif sorted_list[middle] < searchnum:
            left = middle + 1
        ## searchnum이 list[middle]과 같다. 인덱스 반환
        else:
            return middle
    ## while문을 빠져나오는 경우 : right < left
    ## 즉, 리스트 안에 searchnum이 존재하지 않는다
    return -1

alist = [1,2,3,5,6,7,9,10,11,13,14,15,16,17,20,21] ## 정렬된 리스트

print("binary_search(alist, 1) :",binary_search(alist, 1))
print("binary_search(alist, 7) :",binary_search(alist, 7))
print("binary_search(alist, 8) :",binary_search(alist, 8))
print("binary_search(alist, 21) :",binary_search(alist, 21))

