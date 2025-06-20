n, m = map(int, input().split()) # 세로, 가로
r, c, d = map(int, input().split()) # 청소기 좌표, 방향
room = [list(map(int, input().split())) for _ in range(n)]


from collections import deque

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
x, y = r, c

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 청소
    if room[x][y] == 0:
        room[x][y] = 2
        answer += 1
    temp = 0
    for _ in range(4):
        # 반시계 방향 회전
        d -= 1
        if d == -1 :
            d = 3
        nx = x + dx[d]
        ny = y + dy[d]
        # 이동한 곳이 청소하지 않은 빈 칸이 있는 경우 한 칸 전진
        if 0<=nx<n and 0<=ny<m and room[nx][ny] == 0:
            x = nx
            y = ny
            temp = 1
            break
    # 청소되지 않은 빈칸이 없는 경우
    if temp == 0 :
        nx = x-dx[d]
        ny = y-dy[d]
        if 0<=nx<n and 0<=ny<m and room[nx][ny] != 1: # 벽이 아니라면 한 칸 후진
            x = nx
            y = ny
        else :
            break

print(answer)