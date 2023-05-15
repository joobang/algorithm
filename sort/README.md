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