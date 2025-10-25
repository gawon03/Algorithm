import sys
from collections import deque

def topology_sort():
    q = deque()
    # 1. 진입차수가 0인 모든 노드를 큐에 넣는다.
    for i in range(n):
        if indegree[i] == 0:  # 처음은 진입차수가 0인 것부터. 진입차수 0이 시작하는 노드이기 때문
            q.append(i)
    # 2. 큐가 빌 때까지 아래 과정 반복한다.
    while q:
        # 2-1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
        now = q.popleft()
        for i in graph[now]: 
            indegree[i] -= 1
            if indegree[i] == 0:  # 2-2. 새롭게 진입차수가 0이된 노드를 큐에 넣기 & 결과 넣기 
                result[i] = result[now] + 1  # [추가된 부분] 현재 노드 결과에 + 1한(다음 학기) 학기로 넣기 
                q.append(i)

    print(*result)

n, m = map(int, sys.stdin.readline().split())  # 과목수, 선수 조건 수
indegree = [0] * n
result = [1] * n
graph = [[] for i in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)  # a > b
    indegree[b - 1] += 1    # 진입 차수

topology_sort()