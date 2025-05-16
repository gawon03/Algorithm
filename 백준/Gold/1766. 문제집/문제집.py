import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0]*(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

q = []

# 진입 차수가 0인 문제를 최소 힙에 넣어줌.
for idx in range(1, N+1):
    if inDegree[idx] == 0:
        heapq.heappush(q, idx)

res = []

while q:
    # 현재 최소 힙에 들어있는 진입 차수가 0인 문제들 중에서,
    # 문제 번호가 가장 작은(가장 쉬운) 문제를 뽑음
    quest = heapq.heappop(q)
    res.append(quest)
    
    for adj_quest in graph[quest]:
        inDegree[adj_quest] -= 1
        if inDegree[adj_quest] == 0:
            heapq.heappush(q, adj_quest)

print(*res)