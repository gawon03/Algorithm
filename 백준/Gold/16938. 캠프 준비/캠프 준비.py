# 문제 개수(N), 문제 난이도의 합의 최솟값(L), 최댓값(R), 최댓값과 최솟값의 차(X)
N, L, R, X = map(int, input().split())

# 문제의 난이도
level = list(map(int, input().split()))

# 캠프에 사용할 문제 고르는 방법의 수 구하기
# 조건 : 문제는 2개 이상

problem = []
cnt = 0
def dfs(idx):
    global problem, cnt


    # 종료 조건
    if len(problem) >= 2 and max(problem)-min(problem) >= X and L<=sum(problem)<=R:
        cnt += 1

    for i in range(idx, N):
        problem.append(level[i])
        dfs(i + 1)
        problem.pop()

dfs(0)
print(cnt)