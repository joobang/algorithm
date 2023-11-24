from collections import deque

t = int(input())

def bfs(land):
    cnt = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j]:
                cnt += 1
                queue = deque([[i,j]])
                while queue:
                    node_x,node_y = queue.popleft()
                    for z in range(4):
                        nx = node_x + dx[z]
                        ny = node_y + dy[z]
                        if 0 <= nx < n and 0<= ny < m and land[nx][ny]:
                            queue.append([nx,ny])
                            land[nx][ny] = 0
                

    return cnt

for i in range(t):
    m,n,k = map(int, input().split())
    land = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        x,y = map(int, input().split())
        land[y][x] = 1
    
    print(bfs(land))