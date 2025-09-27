n = int(input())
wine = list(int(input()) for _ in range(n))

# 현재 포도주를 마실지 말지를 결정하는 경우
# 1) 현재 포도주와 이전 포도주를 마시고 전전 포도주는 마시지 않는 경우(wine[i]+wine[i-1]+d[i-3])
# 2) 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는 경우 (wine[i]+d[i-2])
# 3) 현재 포도주를 마시지 않는다. (d[i-1])
dp = [0]*n
dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]
if n > 2 :
    dp[2] = max(wine[2]+wine[1], wine[2]+wine[0], dp[1])


for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])

print(max(dp))