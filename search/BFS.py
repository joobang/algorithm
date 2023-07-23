"""
너비우선탐색 가운 노드부터 탐색하는 알고리즘
가장 가까운 노드부터 우선 순위를 가져야하기에, 큐를 이용하여 구현할 수 있다.
deque 이용

동작과정
1. 방문했던 노드 목록을 저장해둔 리트가 필요하다.
2. 다음으로 방문할 노드의 목록을 차례대로 저장할 리스트(큐)를 만들어야한다.
3. 더이상 방문할 노드가 없을 때 까지 루프를 돈다.
"""

from collections import deque

def bfs_iteration(graph, root):
    visited = [] ## visited = 방문한 노드들을 기록한 리스트
    queue = deque([root]) ## bfs는 queue개념을 이용한다.
    while(queue): ## queue에 남은 것이 없을 때까지 반복
        node = queue.pop() ## node : 현재 방문하고 있는 노드
        print('node : ' , node)
        ## 현재 node를 방문한 적 없다. -> visited에 추가
        ## visited에 추가 후, 해당 노드의 자식 노드들을 queue에 추가
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])
        print('visited : ' , visited)
        print('queue : ' , queue)
    return visited

graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

print(bfs_iteration(graph,'A'))
