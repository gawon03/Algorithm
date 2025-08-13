N, M = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

def dfs():

    # 종료 조건
    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return

    for i in range(N):
        if array[i] not in ans:
            ans.append(array[i])
            dfs()
            ans.pop()

ans = []
dfs()