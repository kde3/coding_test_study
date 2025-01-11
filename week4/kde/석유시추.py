from collections import deque
def bfs(start, n, m, land, 석유) :
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    
    startIdx = start[1]
    endIdx = start[1]
    cnt = 1 # 석유량
    while queue :
        y, x = queue.popleft()
        
        for dy, dx in directions :
            ny = y + dy
            nx = x + dx
            
            if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1 :
                land[ny][nx] = -1
                cnt += 1
                startIdx = min(startIdx, nx)
                endIdx = max(endIdx, nx)
                queue.append((ny, nx))
                
    석유.append((startIdx, endIdx, cnt))

def solution(land):
    n = len(land)
    m = len(land[0])
    
    # (startIdx, endIdx, 석유량)
    석유 = []
    
    # 1. bfs 조사
    for i in range(n) :
        for j in range(m) :
            if land[i][j] == 1 :
                land[i][j] = -1
                bfs((i, j), n, m, land, 석유)
    
    # 2. 가장 많은 석유량 리턴
    answer = [0] * m
    for start, end, cnt in 석유 :
        for i in range(start, end + 1) :
            answer[i] += cnt
    
    return max(answer)