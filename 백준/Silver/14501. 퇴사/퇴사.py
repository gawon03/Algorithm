n = int(input())
t = []; p = []

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    
dp = [0] * n


for i in range(n):
    if i != 0:
        if dp[i] != 0:
            dp[i] = max(dp[i], dp[i-1])
        else :
            dp[i] = dp[i] + dp[i-1]
    if t[i] == 1:
        dp[i] = max(dp[i-1] + p[i], dp[i])
    idx = i + t[i] - 1
    if idx < n and t[i] != 1:
        dp[idx] = max(dp[idx], p[i]+dp[i-1])

print(dp[-1]) # 45