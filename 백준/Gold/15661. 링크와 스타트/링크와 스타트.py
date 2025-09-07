N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
ans = 1e9

def summ():
    global ans
    start, link = 0, 0
    for i in range(N):
        for j in range(N):
            if i!=j and visited[i] and visited[j]:
                start += S[i][j]
            elif not visited[i] and not visited[j]:
                link += S[i][j]
    ans = min(ans, abs(start - link))
    return

def dfs(iter):
    # 모든 사람(인덱스)를 다 확인했으면 계산
    if iter == N:
        summ()
        return

    # 현재 사람(iter)을 '스타트 팀'에 포함시킨 경우
    visited[iter] = 1
    dfs(iter + 1) # 다음 사람으로 이동

    # 현재 사람을 '링크 팀'에 포함시킨 경우
    visited[iter] = 0
    dfs(iter + 1) # 다음 사람으로 이동

dfs(0)
print(ans)