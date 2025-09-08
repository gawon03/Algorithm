# 행성 개수(N), ana호가 발사되는 행성의 위치(K)
N, K = map(int, input().split())

# (i, j)의 요소 : i번째 행성에서 j번째 행성에 도달하는 데 걸리는 시간
time = [list(map(int, input().split())) for _ in range(N)]

# 모든 행성을 탐사하는데 걸리는 최소 시간 계산
# 조건 : 탐사 후 다시 시작 행성으로 돌아올 필요 X, 이미 방문한 행성 중복 가능 O

# 방문 기록
visited = [0] * N
visited[K] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])

def find_min(start, cost, cnt):
    global answer
    if N == cnt:
        answer = min(answer, cost)
        return

    for end in range(N):
        if visited[end] == 0:
            visited[end] = 1
            find_min(end, cost + time[start][end], cnt + 1)
            visited[end] = 0

answer = 1e9
find_min(K, 0, 1)
print(answer)
