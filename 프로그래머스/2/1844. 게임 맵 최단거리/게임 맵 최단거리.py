from collections import deque
def solution(maps):
    
    n = len(maps); m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    queue = deque()
    queue.append((0,0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    maps[ny][nx] = 1 + maps[y][x]
                    queue.append((ny, nx))
    
    if maps[n-1][m-1] == 1:
        return -1
    else :
        return maps[n-1][m-1]