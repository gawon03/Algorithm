from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))] # 방문처리를 위한 list
    
    queue = deque()
    queue.append((begin, 0))
    
    while queue:
        word, cnt = queue.popleft()
        
        if word == target:
            answer = cnt
            break
            
        for i in range(len(words)):
            cnt_temp = 0
            if not visited[i]: # 방문하지 않았다면
                for j in range(len(word)): # 철자 하나씩 확인
                    if word[j] != words[i][j]:
                        cnt_temp += 1
                if cnt_temp == 1: # 철자 하나만 다르다면 변경가능
                    queue.append((words[i], cnt+1)) # queue에 추가
                    visited[i] = True # 방문 처리
    return answer

