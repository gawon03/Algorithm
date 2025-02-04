from collections import deque
def check(start, end, visited, graph):
    visited[start] = 1
    visited[end] = 1
    q = deque()
    q.append(end)
    cnt = 1
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                cnt += 1
                q.append(next)
    return cnt

def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n+1)]
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    answer = float("inf")
    for s,e in wires:
        visited = [0] * (n+1)
        res = check(s, e, visited, graph)
        res = abs(n - 2*res)
        answer = min(answer, res)
    return answer