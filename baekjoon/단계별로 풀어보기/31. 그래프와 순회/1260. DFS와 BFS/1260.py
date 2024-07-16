from collections import deque

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
    
def dfs_list(graph,root):
    visited = []
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extendleft(reversed(graph[node]))
        #print('stack : ',queue)
        #print('path : ',visited)
    
    return visited



def bfs_list(graph,root):
    queue = deque([root])
    visited = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
        #print('queue : ',queue)
        #print('path : ',visited)
    
    return visited

bfs_list = bfs_list(graph, v)
dfs_list = dfs_list(graph,v)
for d in dfs_list:
    print(d, end=' ')
    
print()
for b in bfs_list:
    print(b, end=' ')