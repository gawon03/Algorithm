# 물품의 수(N), 준서가 버틸 수 있는 무게(K)
N, K = map(int, input().split())

# 물건의 무게(W), 가치(V)
bag = [list(map(int, input().split())) for _ in range(N)]

# 무게 한도가 j일 때 얻을 수 있는 최대 가치 저장
dp = [0]*(K+1)

# 각 물건에 대해
for W, V in bag:
    # 무게 한도 j를 큰 값부터 작은 값까지 거꾸로 순회
    for j in range(K, W-1, -1):
        # 두 값 중 큰 값을 선택
        # dp[j] : 지금까지 구한 무게 j일 때 최적값
        # V + dp[j - W] : 새 물건을 담았을 때의 가치
        dp[j] = max(dp[j], V + dp[j - W])

print(dp[K])
