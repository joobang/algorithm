"""
    깊이 우선 탐색
    
"""
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','G','H'],
         'D':['B'],
         'E':['B','F'],
         'F':['E'],
         'G':['C'],
         'H':['C']}

def dfs_iteration(graph, root):
    # visited = 방문한 꼭지점들을 기록한 리스트
    visited = []
    # dfs는 stack, bfs는 queue개념을 이용한다.
    stack = [root]
    
    while(stack): #스택에 남은것이 없을 때까지 반복
        node = stack.pop() # node : 현재 방문하고 있는 꼭지점
        print('node : ',node)
        #현재 node가 방문한 적 없다 -> visited에 추가한다.
        #그리고 해당 node의 자식 node들을 stack에 추가한다.
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
        print('visited : ', visited)
        print('stack : ' , stack)
    return visited

#dfs_iteration(graph,'A')

# 재귀를 이용해서 DFS 구현하기
def dfs_recursive(graph, start, visited=[]):
    
    #visited.append(start) ## visited가 재귀를 반복하며 반영된다
    visited = visited + [start] # 이렇게 하면 visited가 서로 다른 리스트를 참초하며 반영이 안된다.
    print(start)
    print(visited) #추가된 print(visited)
    
    for node in graph[start]:
        if node not in visited:
            #dfs_recursive(graph, node, visited) ## visited.append(start) 
            visited = dfs_recursive(graph, node, visited) ## visited = visited + [start]
            
    
    return visited

#dfs_recursive(graph, 'A')

# DFS 경로 탐색하기
# A 부터 H 까지의 경로 구하기
# 방문순서를 순서대로 기록해야함(독자적으로 리스트 할당)

# 새로운 graph
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','F','G'],
         'D':['B'],
         'E':['B','H'],
         'F':['C','H'],
         'G':['C'],
         'H':['E','F']}

paths = []

def dfs_paths(graph, start, end, visited=[]):
    # 그 전에 방문했던 노드들을 기록하고
    # 이번 차례 방문하는 노드를 새로 추가한다.
    visited = visited + [start]
    print('visited : ',visited)
    print('start : ',start)
    print('end : ',end)
    #도착할 경우, paths에 경로를 기록한다.
    if start == end:
        paths.append(visited)
    
    #현재 노드의 자손 노드들 중, 방문하지 않은 노드들에 대해 재귀 호출
    for node in graph[start]:
        if node not in visited:
            dfs_paths(graph, node, end, visited)
            
dfs_paths(graph,'A','H')

print(paths)