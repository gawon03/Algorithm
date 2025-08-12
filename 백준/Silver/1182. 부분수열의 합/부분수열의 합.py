N, S = map(int, input().split())
array = list(map(int, input().split()))
cnt = 0
ans = []

def dfs(start):
    global cnt

    # 종료 조건
    if sum(ans) == S and len(ans) > 0:
        cnt += 1
    
    for i in range(start, N):
        ans.append(array[i])
        dfs(i+1)
        ans.pop()
        
dfs(0)
print(cnt)