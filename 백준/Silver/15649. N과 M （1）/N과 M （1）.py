N, M = list(map(int, input().split()))
ans = []

def dfs():
    # 종료 조건
    if len(ans) == M : # m까지 채우고 출력, 이후 백트래킹
        print(' '.join(map(str, ans)))
        return
    
    for i in range(1, N+1):
        if i not in ans: # 중복 검사
            ans.append(i)
            dfs()
            ans.pop()
            
dfs()