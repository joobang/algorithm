from collections import deque

n = int(input())
land = []
for i in range(n):
    temp = [int(char) for char in input()]
    land.append(temp)

#print(land)

def solution(land):
    answer = []

    def findLand(x,y,land):
        queue = deque([[x,y]])
        total = len(land)
        cnt = 1
        while queue:
            node_x,node_y = queue.popleft()
            #print(node_x, node_y)
            if node_x > 0:
                if land[node_x-1][node_y]:
                    queue.append([node_x-1,node_y])
                    land[node_x-1][node_y] = 0
                    cnt += 1
            if node_x < total-1:
                if land[node_x+1][node_y]:
                    queue.append([node_x+1,node_y])
                    land[node_x+1][node_y] = 0
                    cnt += 1
            if node_y > 0:
                if land[node_x][node_y-1]:
                    queue.append([node_x,node_y-1])
                    land[node_x][node_y-1] = 0
                    cnt += 1
            if node_y < total-1:
                if land[node_x][node_y+1]:
                    queue.append([node_x,node_y+1])
                    land[node_x][node_y+1] = 0
                    cnt += 1
        
        #print(visited)
        return cnt
    
    for x in range(len(land)):
        for y in range(len(land[0])):
            if land[x][y] :
                land[x][y] = 0
                answer.append(findLand(x,y,land))
    
    
    answer.sort()
    return answer

print_solution = solution(land)

print(len(print_solution))
for c in print_solution:
    print(c)