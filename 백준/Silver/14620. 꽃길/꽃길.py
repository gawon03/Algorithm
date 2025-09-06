N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

import copy

amt = 0
answer = 1e9
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y, visited):

    if visited[x][y]:
        return False

    for i in range(4):
        if visited[x+dx[i]][y+dy[i]]:
            return False
    return True


def flower(x, y, temp, amt):

    temp[x][y] = True
    amt += space[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        temp[nx][ny] = True
        amt += space[nx][ny]

    return temp, amt

def dfs(visited, cnt, amt):
    global answer

    # 종료 조건
    if cnt == 3:
        answer = min(answer, amt)
        return answer

    for i in range(1, N-1):
        for j in range(1, N-1):
            if check(i, j, visited):
                # 꽃 피우기
                temp = copy.deepcopy(visited)
                temp, summ = flower(i, j, temp, amt)
                dfs(temp, cnt+1, summ)
                
dfs(visited, 0, 0)

print(answer)