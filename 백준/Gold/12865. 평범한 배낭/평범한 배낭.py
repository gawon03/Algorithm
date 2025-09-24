# 물품의 수(N), 준서가 버틸 수 있는 무게(K)
N, K = map(int, input().split())

# 물건의 무게(W), 가치(V)
bag = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] : 앞에서 i개 물건만 고려했을 때, 최대 무게 j로 달성 가능한 최대 가치
dp = [[0]*(K+1) for _ in range(N+1)]

# 점화식
# dp[i][j] = max(i번째 물건을 담지 않았을 때의 최적값, i번째 물건을 담았을 때의 가치 + 남는 무게에서의 최적값)

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= bag[i-1][0]: # 무게 한도(j)보다 현재 물건 무게가 더 작을 경우(담을 수 있음)
            # 담는 경우 vs 안 담는 경우 중 더 큰 값 선택
            # 담는 경우 : 현재 물건 가치 + 이전 i-1개 물건으로 (j - 현재 무게) 한도에서 얻을 수 있는 최댓값
            # 안 담는 경우 : dp[i-1][j]
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]], dp[i-1][j])
        else: # 담을 수 없는 경우
            dp[i][j] = dp[i-1][j]

print(dp[N][K])