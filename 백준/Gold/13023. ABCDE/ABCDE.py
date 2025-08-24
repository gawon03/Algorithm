# 사람의 수(N), 친구 관계의 수(M)
N, M = map(int, input().split())

friends = list([] for _ in range(N))
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

    
def dfs(no):
    global result, ans

    # 종료 조건
    if result == 1 or len(ans) == 5:
        result = 1
        return

    for i in friends[no]:
        if i not in ans:
            ans.append(i)
            #print('append', i)
            dfs(i)
            ans.pop()
            #print('pop', i)


result = 0
for i in range(N):
    if result == 1:
        break
    ans = []
    dfs(i)

print(result)