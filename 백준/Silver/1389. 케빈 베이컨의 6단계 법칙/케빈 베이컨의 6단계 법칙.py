n, m = map(int, input().split())
info = [set() for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    info[a].add(b)
    info[b].add(a)
    
from collections import deque

total = float("inf")

for i in range(1, n+1):
    visit = [0]*(n+1)
    visit[i] = 1
    queue = deque([i])
    while queue:
        temp = queue.popleft()
        for conn in info[temp]:
            if visit[conn] == 0 :
                visit[conn] = visit[temp]+1
                queue.append(conn)
    if total > sum(visit)-5 :
        total = sum(visit)-5
        answer = i

print(answer)