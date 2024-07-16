from collections import deque

n = int(input())
x = int(input())

graph = {i:[] for i in range(1,n+1)}

for i in range(x):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def findVirus(graph):
    cnt = 1
    visited = []
    queue = deque([1])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
        
    #print(visited)
    
    return len(visited)

#print(graph)
print(findVirus(graph) -1)