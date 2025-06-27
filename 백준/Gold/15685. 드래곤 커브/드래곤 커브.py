# 드래곤 커브 개수
n = int(input())

# 방향:→  ↑  ←  ↓
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# x, y : 드래곤 커브의 시작점
# d : 시작 방향, g : 세대
board = [[0]*101 for _ in range(101)]
for _ in range(n):
    x, y, d, g= map(int, input().split())
    board[y][x] = 1 # 시작 위치

    # 커브 리스트 만들기
    curve = [d]
    for _ in range(g):
        for i in range(len(curve)-1, -1, -1): # 역순으로 90도 반시계방향 회전
            curve.append((curve[i]+1) % 4)

    # 드래곤 커브 만들기
    for i in range(len(curve)): # 커브 방향 동안
        x += dx[curve[i]]
        y += dy[curve[i]]
        board[y][x] = 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

print(result)