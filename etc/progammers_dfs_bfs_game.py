from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])  # 행과 열의 길이
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 이동 가능한 방향 (상, 하, 좌, 우)
    queue = deque([(0, 0, 1)])  # 큐 초기화 (x좌표, y좌표, 거리)
    visited = [[False for _ in range(m)] for _ in range(n)]  # 방문 여부를 확인하는 배열
    visited[0][0] = True  # 시작점 방문 처리

    while queue:
        x, y, dist = queue.popleft()  # 현재 위치와 거리
        print(x,y)
        # 목적지에 도달했을 경우
        if x == n-1 and y == m-1:
            return dist

        # 가능한 모든 방향에 대해 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 맵 안에 있고, 벽이 아니며, 아직 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True

    return -1  # 경로가 없는 경우

# 테스트
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
