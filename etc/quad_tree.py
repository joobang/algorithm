
from collections import deque

def solution(a,b):
    a_arr = [[0 for _ in range(32)] for _ in range(32)]
    b_arr = [[0 for _ in range(32)] for _ in range(32)]
    a_queue = deque(a)
    b_queue = deque(b)
    # 1 data[x ~ x + size/2][y + size/2 ~ y + size]
    # 2 data[x ~ x + size/2][y ~ y + size/2]
    # 3 data[x + size/2 ~ x + size][y ~ y + size/2]
    # 4 data[x + size/2 ~ x + size][y + size/2 ~ y + size]
           
    def makePixel(queue,x,y,size,data):
        s = queue.popleft()
        if s == "p":
            size = size//2
            makePixel(queue,x,y+size,size,data)
            makePixel(queue,x,y,size,data)
            makePixel(queue,x+size,y,size,data)
            makePixel(queue,x+size,y+size,size,data)
        elif s == "w":
            for i in range(x,x+size):
                for j in range(y,y+size):
                    data[i][j] = 0
        elif s == "b":
            for i in range(x,x+size):
                for j in range(y,y+size):
                    data[i][j] = 1
                    
    makePixel(a_queue,0,0,32,a_arr)
    makePixel(b_queue,0,0,32,b_arr)
    
    cnt = 0
    for i in range(32):
        for j in range(32):
            if a_arr[i][j] == 1 or b_arr[i][j] == 1:
                cnt += 1
            
    
    return cnt



print(solution("ppwwwbpbbwwbw", "pwbwpwwbw"))
print(solution("b", "w"))