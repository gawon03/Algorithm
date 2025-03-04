def solution(triangle):
    N = len(triangle)
    lst = [[0]*i for i in range(1, N+1)]
    lst[0] = triangle[0]
    
    for i in range(N-1):
        for j in range(len(triangle[i])):
            lst[i+1][j] = max(lst[i+1][j], lst[i][j]+triangle[i+1][j])
            lst[i+1][j+1] = lst[i][j]+triangle[i+1][j+1]
    return max(lst[-1])