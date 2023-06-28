# 정렬 알고리즘(sort algoritm)

시간 복잡도: 특정한 크기의 입력에 대하여 알고리즘의 수행 시간 분석

시간복잡도는 **특정 알고리즘이 어떤 문제를 해결하는데 걸리는 시간**을 의미

공간 복잡도: 특정한 크기의 입력에 대하여 알고리즘의 메모리 사용량 분석

공간 복잡도란 **작성한 프로그램이 얼마나 많은 공간(메모리)을 차지하느냐를 분석하는 방법**

시간과 공간은 반비례적 경향이 있음

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbLkiqp%2FbtrPynMAclg%2FWMUb1dIKSR0tDtoPiUkAk0%2Fimg.png)
시간 복잡도 성능 비교

- O(1) : 입력자료의 수에 관계없이 일정한 실행시간을 갖음
- O(logn) : 입력자료의 수에 따라 시간이 흐를수록 시간이 조금씩 증가
- O(n) : 입력 자료의 수에 따라 선형적인 실행 시간이 걸리는 경우 - 입력자료마다 일정 시간 할당
- O(nlogn) : 큰 문제를 일정 크기 갖는 문제로 쪼개고(logn+logn+ .. + logn) 다시 그것을 모으는 경우
- O(n^2) : 이중 루프내에서 입력 자료를 처리할 때
- O(n^3) : 삼중 루프 내에서 입력자료 처리할 때

### 시간복잡도가 빠른순
O(1) > O(logn) > O(n) > O(nlogn) > O(n^2) > O(n^3) > O(2^n) > O(n!)

정렬알고리즘에서 시간복잡도
![img](https://raw.githubusercontent.com/junghyun100/junghyun100.github.io/master/images/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84.PNG)

자료구조에서의 시간복잡도
![img](https://raw.githubusercontent.com/junghyun100/junghyun100.github.io/master/images/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84/%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%842.PNG)

## 1. 선택 정렬(Selection Sort)

선택정렬은 데이터 중 가장 작은 값의 데이터를 선택하여 앞으로 보내는 정렬.


![img](https://blog.kakaocdn.net/dn/cZQbUG/btrPyuSnfNC/Ko9PhsE7CRoJqEs5ZKN48K/img.gif)

1. 주어진 배열 중에 최소값을 찾는다.
2. 그 값을 맨 앞에 위치한 값과 교체한다. (swap)
3. 바꿔서 fixed 된값을 제외하고 나머지 배열 중에 최소값을 찾는다.

## 2. 삽입 정렬(Insertion Sort)

![img](https://blog.kakaocdn.net/dn/yjIQN/btrPzM5xqPz/mDQr7ppZeDFh2xpZsKS8w0/img.gif)

- 삽입 정렬은 데이터를 순서대로 뽑아서 적절한 위치를 찾아 삽입함으로써 완성하는 정렬.
- 삽입 정렬의 시간 복잡도는 O(N²)이며 Worst, Average는 동일하고 이미 정렬되어 있는 Best의 경우 O(N)입니다. 
- 무조건 위치를 변경하는 선택 정렬과 시간 복잡도가 같지만 필요할 때에 삽입한다는 점에서 연산수가 적어지므로 효율적입니다. 
- 이미 정렬되어 있는 데이터가 많다면 빠른 알고리즘입니다.

## 3. 버블 정렬(Bubble Sort)

![img](https://blog.kakaocdn.net/dn/kTpcI/btqO13hKM3O/hsZY59VnJYPiQVKikxw4N0/img.gif)

- 버블 정렬은 매번 연속된 두개 인덱스를 비교하여, 정한 기준의 값을 뒤로 넘겨 정렬하는 방법.
- 오름차순으로 정렬하고자 할 경우, 비교시마다 큰 값이 뒤로 이동하여, 1바퀴 돌 시 가장 큰 값이 맨 뒤에 저장된다.
- 맨 마지막에는 비교하는 수들 중 가장 큰 값이 저장되기 때문에, (전체 배열의 크기 - 현재까지 순환한 바퀴 수) 만큼만 반복해 주면 된다.
- 버블 정렬은 다음과 같은 순서로 작동한다.
   1. 0번째 원소와 1번째 원소를 비교 후 정렬
   2. 1번째 원소와 2번째 원소를 비교 후 정렬

      …
   3. n-1번째 원소와 n번째 원소를 비교 후 정렬
- 시간복잡도 O(N²)

## 4. 힙 정렬(Heap Sort)

- 완전 이진트리에서 파생된 heap 특성을 사용하여 정렬하는 알고리즘
- 힙은 부모의 값이 자식의 값보다 항상 크거나 항상 작다라는 조건을 만족하는 완전이진트리 형태의 자료구조이다.
- 완전이진트리는 자식 노드를 왼쪽부터 채워나가는 형태의 자료구조이다.
- 시간복잡도 O(nlogn)

 최대힙 (Max Heap) - 부모 노드 값은 항상 자식 노드 값보다 크다.
 최소힙 (Min Heap) - 자식 노드 값은 항상 부모 노드 값보다 크다.
 ![img](https://blog.kakaocdn.net/dn/bJ0bZp/btqO71C7qgs/t5mSrqMNjP71Jkohu8tBq1/img.gif)
 힙 정렬은 최대힙의 특성을 가지고 정렬을 구현한다.
 - 힙 정렬은 다음과 같은 순서로 작동한다.
 	
    1. 최대 힙의 루트 노드를 마지막 배열 값과 교환. 가장 큰 값을 마지막 배열에 저장. 그리고 가장 크고 마지막 배열에 있는 값을 힙에서 제거. 
 ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FG2ks9%2FbtriYXTCHyg%2FwqvECzpCoyr7fNCEd0DM1k%2Fimg.png)
    2. 다시 힙을 재구조화시킴으로써 10을 제외한 최대 힙이 root자리를 다시 가져가게 됨
     ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbWKJfX%2Fbtri7R4XSep%2FMydzdHgalThNV0kCA4qEbK%2Fimg.png)
    3. 새로 생신 최대 힙을 배열에 10 을제 외한 마지막 배열과 교환. 즉 루트 노드인 9는 1이 있는 위치로 바뀌게 됩니다. 
    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcVueVD%2Fbtri1cJOthF%2FL0rrUzthG4xlJyMkZGyQSK%2Fimg.png)
    4. 위 과정을 반복하여줍니다. 
    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcVueVD%2Fbtri1cJOthF%2FL0rrUzthG4xlJyMkZGyQSK%2Fimg.png)
    5. 모두 정렬될 때까지 반복하겠습니다. 
    ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FWejq6%2Fbtri7Q53QJM%2Fv1B0mcRNxW9oQ8tGzvxlpk%2Fimg.png)
    
## 5. 병합정렬(Merge Sort)

- 둘 이상의 부분집합으로 가르고, 각 부분집합을 정렬한 다음 부분집합들을 다시 정렬된 형태로 합치는 방식.
(분할 정복 방식)
- 추가로 병합 정렬은 퀵 정렬과 달리 정렬을 할 때 데이터 크기만큼의 추가 공간이 필요하므로 제자리 정렬 (in-place sort)이 될 수는 없다.
- 예제에서 보이는 것과 같이 8 -> 4 -> 2 -> 1 식으로 전반적인 반복의 수는 점점 절반으로 줄어들 기 때문에 O(logN) 시간이 필요하며, 각 패스에서 병합할 때 모든 값들을 비교해야 하므로 O(N) 시간이 소모됩니다. 따라서 총 시간 복잡도는 O(NlogN) 입니다.
- 두 개의 배열을 병합할 때 병합 결과를 담아 놓을 배열이 추가로 필요합니다. 따라서 공간 복잡도는 O(N) 입니다.

병합 정렬의 예시

 ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FyPTS3%2FbtrIseBpDC3%2Fq3Y9mpsY9kJunnVbj6p3tk%2Fimg.png)

병합 정렬 병합 과정

1. 두 개의 리스트의 값을 처음부터 비교해서 두 개의 리스트의 값 중에 작은 값을 새로운 리스트로 옮긴다.
2. 두 개의 리스트 중 하나의 리스트가 끝날 때까지 반복한다.
3. 하나의 리스트가 끝나게 되면 남은 리스트의 값을 모두 새로운 리스트로 옮긴다.
 ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtgijT%2FbtrItuxkweb%2FX8aTrmEpx9JiVdSrJyEKNk%2Fimg.png)

## 6. 퀵정렬(Quick Sort)

- 데이터 집합내에 임의의 기준(pivot)값을 정하고 해당 피벗으로 집합을 기준으로 두개의 부분 집합으로 나눈다. 한쪽 부분에는 피벗값보다 작은값들만, 다른 한쪽은 큰값들만 넣는다
- 퀵 정렬은 분할 정복(divide and conquer) 방법을 통해 리스트를 정렬
병합 정렬(Merge Sort)와 달리 퀵 정렬은 리스트를 비균등하게 분할
- 시간 복잡도는 O(NlogN) 최악은 O(N²)
예시 ) 정렬되어 있는 경우를 또 정렬하는 경우
[1,2,3,4] 인 배열이 있을 때 1을 기준점으로 두고 두 개의 부분배열로 나누면 4번의 연산이 필요하다. 현재 1보다 작은 배열은 없는 상태이고 큰 배열엔 [2,3,4]가 있으므로 [2,3,4]를 또 나누면 3번의 연산이 필요 ...
이렇게 총 4+3+2+1로 O(n^2)의 시간복잡도를 갖게 된다.

 ![img](https://blog.kakaocdn.net/dn/sVgeg/btqO6hT6nVq/APxheX0siKi3SJRHxvx3n0/img.gif)
 
퀵정렬 과정은 다음과 같다.

1. 각 부분에서 맨 첫값을 pivot(key)로 잡아준다.
2. 인덱스를 key부터 늘려가면서 pivot값보다 큰 값을 찾는다.
3. 인덱스를 끝에서부터 줄여가면서 pivot값보다 작은 값을 찾는다.
4. 큰 값과 작은 값을 찾으면 둘이 교체해준다.
5. 4에서 만약 큰 값과 작은 값이 교차하는 경우(인덱스 순서가 바뀌면) 작은 값과 pivot값을 바꿔준다.
6. 1~5가 1세트이다. 즉, 하나의 부분에서 발생하는 정렬코드이다. 반으로 나눠주면서 쪼개지는 부분마다 계속해서 같은 정렬코드를 구현할 수 있도록 재귀함수를 쓴다(자기자신을 불러온다)

 ![img](https://velog.velcdn.com/images%2Fywc8851%2Fpost%2Fd50511a1-8fd5-4385-bd34-36e2b31579f8%2Fimage.png)
 
#### 최악의 시간복잡도를 방지하기 위한 방법
- 랜덤화
배열의 랜덤한 두 개의 index를 뒤바꾸어주는 방식으로 배열이 정렬되어 있지 않도록 만든다.

- 랜덤 기준점 선택
기준점을 난수를 발생시켜 선택하는 방법으로, 정렬되었거나, 정렬에 가까운 배열에서 최악을 선택하는 횟수가 적어질 것이다.

- Median Of Three Pivot
기준점을 선택할 때 3개의 원소를 후보로 두고 그 중간 값을 선택하는 방법으로 이렇게 기준점을 선택하면 최악의 경우는 반드시 피할 수 있다.

 ## 7. 기수정렬(Radix Sort)
 
 - 기수정렬은 낮은 자리수부터 비교하여 정렬해 간다는 것을 기본 개념으로 하는 정렬 알고리즘입니다.
 - 기수정렬은 비교 연산을 하지 않으며 정렬 속도가 빠르지만 데이터 전체 크기에 기수 테이블의 크기만한 메모리가 더 필요합니다.
 - 각 데이터를 자릿수를 기준으로 분류하므로, 가장 큰 자릿수를 D라고 했을 때 0(DN)의 시간 복잡도를 가진다.
 
  ![img](https://blog.kakaocdn.net/dn/bjN67K/btqO13Py7dC/E8GVOHS9rpk3TvgagRnhsk/img.gif)
  
기수 정렬의 종류

1. LSD (Least Significant Digit) 방식의 정렬​
가장 작은 자릿수부터 정렬을 진행 (숫자로 치면 일의 자리수부터)
가장 작은 자릿수부터 큰 자릿수까지 비교해야 한다는 단점이 있지만, 코드 구현이 MSD에 비해 간결하다
 
2. MSD (Most Significant Digit) 방식의 정렬​
가장 큰 자릿수부터 정렬을 진행
LSD와 비교했을 때 정렬 상태 확인등의 추가 작업이 필요하지만, 중간에 정렬이 완료될 수 있다는 장점이 있다
 

기수 정렬 과정
	
   1. 기수만큼 큐(Queue)를 이용해 저장공간 (Bucket)을 생성한다.
   2. 데이터의 1의 자리를 기준으로 버킷에 넣는다.
   3. 버킷에 저장된 데이터를 순서대로 꺼내 기존 데이터에 덮어쓴다.
   4. 데이터의 10의 자리를 기준으로 버킷에 넣는다.
   5. 마지막 자리수까지 정렬의 기준이 될 자리수를 늘리며 정렬한다.
   
 ![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcKTPl1%2FbtrkxNUPKGR%2FGx39rpLR13KJzsJRtucfJ0%2Fimg.jpg)
 
-------
## 출처
https://hyo-ue4study.tistory.com/68
https://underdog11.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Heapsort-%ED%9E%99%EC%A0%95%EB%A0%AC
https://www.daleseo.com/sort-merge/
https://propercoding.tistory.com/198
https://velog.io/@ywc8851/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%80%B5-%EC%A0%95%EB%A0%AC-Quick-Sort
https://datascientistchocobread.tistory.com/64
https://banjjak1.tistory.com/52




