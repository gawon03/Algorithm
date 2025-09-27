N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]

# 누적합 배열 (인덱스 1부터 쓰기 위해 N+1)
dp = [[0] * (N+1) for _ in range(N+1)]

# 누적합 계산
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = board[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# 질의 처리
for x1, y1, x2, y2 in info:
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)