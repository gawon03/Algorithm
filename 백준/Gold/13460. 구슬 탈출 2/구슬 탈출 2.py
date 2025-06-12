from collections import deque

n, m = map(int, input().split()) # 행, 열
board = [list(input()) for _ in range(n)] # 보드
visited = [] # 방문 위치

# 이동 가능 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def getPos():
    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                rx, ry = x, y
            if board[x][y] == 'B':
                bx, by = x, y
    return rx, ry, bx, by

# 현재 위치(x,y)에서 해당 방향(dx, dy)으로 기울여서 이동한 위치(x, y)와 칸 수(cnt) 얻기
def move(x, y, dx, dy):
    cnt = 0 # 한 번 기울일 때 이동한 칸 수
    # 이동할 위치가 벽이 아니고, 현재 위치가 구멍일 때까지 반복해서 한 칸씩 이동
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solution():
    # R, B 구슬 위치 얻기
    rx, ry, bx, by = getPos()

    # 현재 위치 세팅
    q = deque()
    q.append((rx, ry, bx, by, 1)) # R위치(rx, ry), B위치(bx, by), 기울인 횟수(result)
    visited.append((rx, ry, bx, by))


    # 더이상 구슬이 움직이지 않을 때까지 반복(성공하거나 실패할 때까지)
    while q:
        rx, ry, bx, by, result = q.popleft()

        # 구슬이 움직이는 횟수는 10번 이하여야 함
        if result > 10:
            break

        # 4가지 기울이기 동작 시행
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i]) # 빨간 구슬 기울이기 시행
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i]) # 파란 구슬 기울이기 시행
        # 만약 구멍을 만났다면 해당 구슬 좌표의 위치는 구멍에서 멈춤
        # 구멍없이 벽을 만났다면 해당 좌표는 벽 앞에서 멈추게 됨

            # 파란 구슬이 구멍에 도착했다면 실패이므로 방문 기록하지 않고 pass
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 구멍에 도착했다면 성공이므로 기울이기 동작 횟수 출력 후 return
            if board[nrx][nry] == 'O':
                print(result)
                return

            # 빨간 구슬과 파란 구슬이 같은 위치일 경우(겹치는 경우)
            if nrx == nbx and nry == nby:
                # 움직인 칸수가 더 많은 구슬이 다른 구슬보다 한 칸 적어야함
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 1번의 기울이기를 마치고 도달한 좌표 값이 이전에 방문한 적이 없다면 큐 추가
            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, result+1))
    print(-1)

solution()