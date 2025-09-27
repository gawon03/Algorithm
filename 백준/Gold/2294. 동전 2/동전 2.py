n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))

# dp[i] = 금액 i를 만드는 데 필요한 최소 동전 개수
dp = [1e9] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(-1 if dp[k] == 1e9 else dp[k])
