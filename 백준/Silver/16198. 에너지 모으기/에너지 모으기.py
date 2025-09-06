N = int(input())
weight = list(map(int, input().split()))

import copy

def dfs(weight, cnt, n):
    global answer, temp

    # 종료 조건
    if cnt == N-2:
        answer = max(answer, temp)
        return

    for i in range(1, n-1):
        wght_copy = copy.deepcopy(weight)
        temp += wght_copy[i-1]*wght_copy[i+1]
        wght_copy = wght_copy[:i]+wght_copy[i+1:]
        dfs(wght_copy, cnt+1, n-1)
        temp -= weight[i-1]*weight[i+1]

answer = 0
temp = 0

dfs(weight, 0, N)
print(answer)