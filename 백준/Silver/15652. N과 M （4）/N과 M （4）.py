N, M = map(int, input().split())

def dfs(idx):

    # 종료 조건
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return

    for i in range(idx, N+1):
        ans.append(i)
        dfs(i)
        ans.pop()

ans = []
dfs(1)