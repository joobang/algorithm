"""
    순열
    서로 다른 n개의 대상에서 r개를 뽑아 일렬로 배열한 것을 말하고 그 경우의 수는 nPr로 표현한다.(n>=r) 그리고
    n과 r이 같을 때 순열의 경우의 수는 계승(factorial,n!)이 된다.
    nPr = n!/(n-r)!
"""
# 1. 재귀
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        #print('chosen : ', chosen)
        #print('used : ', used)
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	    # 3.
        for i in range(len(arr)):
            #print('i : ',i)
            #if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
                #print('after chosen : ', chosen)
                #print('after used : ', used)
                
    generate([], used)
    
#permutation('ABCD', 2)
#permutation([1, 2, 3, 4, 5], 3)
#permutation('AABC', 2)

"""
    1. 먼저 사용자가 원하는 arr 과 r 을 받는다. 
        그리고 arr 을 오름차순 정렬하는데 여기서는 큰 의미가 있지는 않고 단순히 출력을 이쁘게 하기 위해서이다.
        그리고 used 변수를 만드는데, 이 변수는 i 번째 값을 썼는지 저장하는 데 쓰인다. 
        우리는 모든 순열을 하나씩 만들고 출력하는데 당연히 중복값은 저장되어서는 안 된다.
    2. 실제 순열을 만들 generate 함수를 생성한다.
        먼저 chosen 변수는 순열의 원소를 저장되는 변수인데 이 배열에 값을 하나씩 추가하다가 그 개수가 r 이 되는 순간 하나의 순열이 만들어진 것이므로 출력 후 종료한다.
    3. 이 함수의 핵심이다. 
        모든 순열은 arr 의 0부터 i-1 번째 값으로 시작하기에 for 문으로 다 만들어야 한다.
        그리고 chosen 에 값 추가 후, used 에 해당 변수를 사용했다고 체크한다.
        그 다음 다시 generate 를 반복한다. 하나가 만들어진 후에는 그 값을 uncheck해줘야 한다.
"""

# 2. 내장패키지 모듈

from itertools import permutations

arr = ['A','B','C']
#print(list(permutations(arr,2)))

# 3. 전체 순열 뽑는 경우(r개가 아닌 전체)

# DFS로 모든 경우의 수를 하나씩 구하되, 각 경우의 수에 같은 요소가 없도록 함으로써 순열을 구현한다

l = ['a', 'b', 'c']
visited = [0 for _ in range(len(l))]
answer = []

def dfs(cnt, list):
    if cnt == len(l):
        answer.append(list[:])
        return

    for i, val in enumerate(l):
        # 만약 방문했다면 건너 뛰기(순열을 위함)
        if visited[i] == 1:
            continue
        # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)
        visited[i] = 1

        dfs(cnt+1, list)
        # 방금 전 list에 추가한 값과 방문 한 것을 되돌려주기
        list.pop()
        visited[i] = 0

dfs(0, [])
#print(answer)

"""
    조합
    순열과 달리 조합(combination)은 같은n개 중에 r개를 뽑되, 순서를 고려하지 않는다.
    nCr = n!/(n-r)!r!
    
"""

# 1. 재귀
def combination(arr, r):
    # 사용된 원소를 저장할 배열을 만든다.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 선택리스트에 조의 원소를 저장하다가 갯수가 r개가 되면 출력 후 함수를 종료한다.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# chosen(뽑은 조합 원소)가 없으면 start = 0으로
        # 그 외에는 뽑은 조합의 가장 마지막 요소를 값의 인덱스 출력
        # arr = [1, 2, 3, 4]
        # 예를들어 chosen = [1, 2]를 뽑은 상태라면 start = arr.index(2) 이므로 1이고
        # 거기에 1을 더해 최종 : 2
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        # nxt = 2부터 시작
        for nxt in range(start, len(arr)):
            # 만약 아직 뽑지 않았고, ~~ 조건이라면
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
            # if used[nxt] == 0 :
                # 다음 요소를 뽑고 방문처리한다.
                chosen.append(arr[nxt])
                used[nxt] = 1
                # 다 뽑았으면 마지막 요소부터 pop하고 방문해제한다.
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])


#combination([1, 2, 3, 4], 3)


#combination('ABCDE', 2)
#combination([1, 2, 3, 4, 5], 3)

"""
    1. 입력은 순열 때와 같다. 배열도 마찬가지로 정렬한다.
    2. 조합을 만드는 generate 함수를 만든다. 
        순열과 마찬가지로 chosen 에 저장된 아이템 개수가 r 개이면 조합이 하나 완성된 것이기 때문에 값을
        출력하고함수를 종료시킨다.
    3. for 문을 돌리되, 시작을 chosen 에 저장된 마지막 값 다음으로 정한다.
        이는 아까 순열함수와 대비되는 부분으로, 조합은 순열과 달리 순서를 고려하지 않고 뽑기 때문에, 
        가짓수를 제한해줘야 한다. start 가 chosen 이 비어있을 경우 0이 되는 것도 참고한다.
        빈값일 때는 그냥 0을 넣어야 한다.
"""

# 2. 내장 패키지 모듈 사용

from itertools import combinations

arr = ['A','B','C']
#print(list(combinations(arr, 2)))

"""
    중복 제거 문제
    정답은 중복되는 원소에 등장하는 순서를 정하는 것이다. 
    예제에서 ‘A’가 두 개면, ‘A’에 보이지 않는 0, 1의 인덱스를 줘서 순서를 지켜서 등장하게 하면 중복이 나오지 않는다.
    if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
        
    1. i 가 0일 때:
        i 가 0이면 배열의 첫 원소이기 때문에 바로 쓰면 된다.
    2. arr[i-1] != arr[i] 일 때:
        지금은 arr 이 정렬되어 있다. 이때 i 번째 원소가 i-1 번째와 다르면 그냥 ‘B’, ‘C’ 처럼 서로 다른 원소이기 때문에 바로 쓴다.
    3. used[i-1] 일 때:
        가령 i 번째 원소가 두 번째 ‘A’이면, 중복을 피하기 위해 첫 번째 ‘A’가 사용된 상태여야만 쓸 수 있다. 그래서 i-1 번째 원소가 쓰인 상태인지 확인한다.
        이렇게 하면 순열일 때 중복을 피할 수 있다.
"""

def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
        for i in range(len(arr)):
	    # 3.
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)


#permutation('ABC', 2)

def combination(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])


#combination('ABC', 2)
#combination([1, 2, 3, 4, 5], 3)

"""
    A,B,C에서 2개문자를 뽑는경우
    순열 -> AB,AC,BA,BC,CA,CB
    중복순열 -> AB,AC,BA,BC,CA,CB + AA, BB, CC
    조합 -> AB,AC,BC
    중복조합 -> AB,AC,BC + AA, BB, CC
"""

# 중복순열

from itertools import product

arr = ['A','B','C']
#print(list(product(arr, repeat = 2)))

# 중복 조합

from itertools import combinations_with_replacement

print(list(combinations_with_replacement(arr, r = 2)))

## 출처 : https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations