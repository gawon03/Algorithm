def dfs(idx):
    global ans

    if len(ans) == 6:
        print(' '.join(map(str, ans)))
        return

    for i in range(idx, k):
        ans.append(s[i])
        dfs(i+1)
        ans.pop()

while True:
    temp = list(map(int, input().split()))

    if temp == [0]:
        break

    k, s = temp[0], temp[1:]
    ans = []
    dfs(0)
    print(' ')