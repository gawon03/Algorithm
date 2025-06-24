n = int(input()) # 수의 개수
lst = list(map(int, input().split())) # 수열
operators = list(map(int, input().split())) # +, -, x, %

mx = -1e9
mn = 1e9

def dfs(cnt, temp):
    global mx, mn

    if cnt == n-1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return

    if operators[0] != 0: # 덧셈
        operators[0] -= 1
        dfs(cnt+1, temp+lst[cnt+1])
        operators[0] += 1

    if operators[1] != 0: # 뺄셈
        operators[1] -= 1
        dfs(cnt+1, temp-lst[cnt+1])
        operators[1] += 1

    if operators[2] != 0: # 곱셈
        operators[2] -= 1
        dfs(cnt+1, temp*lst[cnt+1])
        operators[2] += 1

    if operators[3] != 0: # 나눗셈
        operators[3] -= 1
        dfs(cnt+1, int(temp/lst[cnt+1]))
        operators[3] += 1


dfs(0, lst[0])
print(mx)
print(mn)
