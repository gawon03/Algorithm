N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

MAX_COST = sum(cost)
dp = [0] * (MAX_COST + 1)  # dp[c] = 비용 c로 얻을 수 있는 최대 메모리

for i in range(N):
    m, c = memory[i], cost[i]
    for money in range(MAX_COST, c-1, -1):  # 뒤에서 앞으로(0/1 배낭)
        dp[money] = max(dp[money], dp[money - c] + m)

# 메모리 M 이상이 되는 최소 비용 찾기
for money in range(MAX_COST + 1):
    if dp[money] >= M:
        print(money)
        break
