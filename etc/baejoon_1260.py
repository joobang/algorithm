n,m,v = map(int, input().split()) 
# 앞의 글자는 n, 뒤의 글자는 m으로 할당됨.

graph = {i:[] for i in range(1, n+1)}
#print(graph)
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    

for key in graph:
    graph[key].sort()

#print(graph)
    
def dfs(graph, start, visited=[]):
    visited.append(start)
    
    #print('start : ',start)
    #print('visited : ',visited)
    
    for node in graph[start]:
        if node not in visited:
            dfs(graph,node,visited)
            
    return visited

dfs_list = dfs(graph, v)

from collections import deque
def bfs(graph, root):
    visited = [] ## visited = 방문한 노드들을 기록한 리스트
    queue = deque([root]) ## bfs는 queue개념을 이용한다.
    while(queue): ## queue에 남은 것이 없을 때까지 반복
        node = queue.pop() ## node : 현재 방문하고 있는 노드
        #print('node : ' , node)
        ## 현재 node를 방문한 적 없다. -> visited에 추가
        ## visited에 추가 후, 해당 노드의 자식 노드들을 queue에 추가
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])
        #print('visited : ' , visited)
        #print('queue : ' , queue)
    return visited

bfs_list = bfs(graph, v)

for d in dfs_list:
    print(d, end=' ')
    
print()
for b in bfs_list:
    print(b, end=' ')