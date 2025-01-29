from collections import deque

def solution(priorities, location):
    queue = deque((i,j) for i,j in enumerate(priorities))
    answer = []
    while queue:
        q = queue.popleft()
        if any(q[1] < p[1] for p in queue):
            queue.append(q)
        else :
            answer.append(q)
    for a in answer:
        if a[0] == location:
            return answer.index(a) + 1