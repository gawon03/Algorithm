def find(ways):
    visited = [False]*N
    for i in range(1,N):
        if abs(ways[i] - ways[i-1]) > 1: # 조건 2
            return False
        
        if ways[i-1] > ways[i] : # 왼쪽 지점이 더 클 때
            for j in range(L): # 경사로 크기까지
                if i + j >= N or ways[i] != ways[i+j] or visited[i+j]: # 경사로가 밖을 벗어나거나, 길이가 다르거나, 이미 설치했다면 (조건 4)
                    return False
                if ways[i] == ways[i+j]: # 좌우 높이가 같으면 (조건 1) 
                    visited[i+j] = True # 경사로 놓자 
                    
        elif ways[i-1] < ways[i] : # 오른쪽 지점이 더 클 때
            for j in range(L):
                if i - j - 1 < 0 or ways[i-1] != ways[i - j - 1] or visited[i - j - 1]: # 경사로가 밖을 벗어나거나, 길이가 다르거나, 이미 설치했다면 (조건 4)
                    return False
                if ways[i-1] == ways[i-j-1]: #조건 1
                    visited[i-j-1] = True
    return True


N, L = map(int, input().split())
way = [list(map(int, input().split())) for _ in range(N)]
cross = list(zip(*way)) 
result = 0
for i in range(N) :
    if find(way[i]): # 가로
        result += 1
    if find(cross[i]): #세로
        result += 1
print(result)