# 목표 고객 수(C), 홍보할 수 있는 도시의 개수(N)
C, N = map(int, input().split())

# 홍보 비용, 고객 수
PR = [list(map(int, input().split())) for _ in range(N)]

# 호텔 고객을 적어도 C명 늘리기 위해 투자해야하는 돈의 최솟값 구하기
# C명에 대한 최소비용을 출력할 때, C명보다 많은 고객 수에서 최소비용이 나올 수 있기 때문, 주어지는 비용은 최대 100원을 넘지 않음
dp = [1e9]*(C+100)
dp[0] = 0
for cost, cnt in PR:
    for i in range(cnt, C+100):
        dp[i] = min(dp[i], dp[i-cnt]+cost)

print(min(dp[C:]))