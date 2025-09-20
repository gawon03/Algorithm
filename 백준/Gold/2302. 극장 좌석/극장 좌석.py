N = int(input())
M = int(input())
vip = list(int(input()) for _ in range(M))

# dp[i] = 연속된 좌석이 i개 있을 때 가능한 배치의 경우의 수
# dp[i] = dp[i-1] + dp[i-2]
# dp[i-1] : 마지막 사람이 제자리에 앉는 경우
# dp[i-2] : 마지막 두 명이 서로 자리를 바꾼 경우
# 피보나치 수열 구조가 됨.

dp = [0] * (N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
if M > 0:
    pre = 0
    for j in range(M):
        answer *= dp[vip[j] - 1 - pre] # 각 구간의 경의 수를 곱셈(구간 간에는 서로 독립적이므로)
        pre = vip[j]
    answer *= dp[N - pre]
else :
    answer = dp[N]

print(answer)