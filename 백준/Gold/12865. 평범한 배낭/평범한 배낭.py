# 물품의 수(N), 준서가 버틸 수 있는 무게(K)
N, K = map(int, input().split())

# 물건의 무게(W), 가치(V)
bag = [list(map(int, input().split())) for _ in range(N)]

dp = [0]*(K+1)
for W, V in bag:
    for j in range(K, W-1, -1):  # 뒤에서 앞으로!
        dp[j] = max(dp[j], V + dp[j - W])
print(dp[K])