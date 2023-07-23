"""
    순열
    서로 다른 n개의 대상에서 r개를 뽑아 일렬로 배열한 것을 말하고 그 경우의 수는 nPr로 표현한다.(n>=r) 그리고
    n과 r이 같을 때 순열의 경우의 수는 계승(factorial,n!)이 된다.
    nPr = n!/(n-r)!
"""

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
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
            #if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
                #print('after chosen : ', chosen)
                #print('after used : ', used)
                
    generate([], used)
    
permutation('ABCD', 2)
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

