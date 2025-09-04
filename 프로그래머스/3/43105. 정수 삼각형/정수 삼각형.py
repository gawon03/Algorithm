def solution(triangle):
    N = len(triangle)
    dp = [[0]*i for i in range(1, N+1)]
    dp[0] = triangle[0]
    
    for i in range(N-1):
        for j in range(len(triangle[i])):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+triangle[i+1][j])
            dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]
    return max(dp[-1])