N = int(input())

def dfs():
    global ans
    
    # 종료 조건
    if len(ans) == N:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()

ans = []
dfs()