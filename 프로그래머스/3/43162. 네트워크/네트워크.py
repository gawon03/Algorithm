def solution(n, computers):
    visited = [False]*n
    answer = 0
    
    def dfs(pc):
        visited[pc] = True # 방문 처리
        for idx, connected in enumerate(computers[pc]): # 연결 정보 하나씩 확인
            if connected and not visited[idx]: # 연결되어 있고 방문하지 않았다면 이동
                dfs(idx)
    
    for pc in range(n):
        if visited[pc] == 0: # 방문하지 않은 PC 확인
            dfs(pc)
            answer += 1 # 한 번의 확인(네트워크)마다 1추가
    return answer