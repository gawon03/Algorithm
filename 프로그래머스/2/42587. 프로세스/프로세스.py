from collections import deque

def solution(priorities, location):
    queue = deque((i, j) for i, j in enumerate(priorities))
    answer = [] # 실행된 프로세스
    while queue:
        q = queue.popleft()
        # 우선순위가 더 높은 프로세스가 하나라도 있으면 큐에 다시 추가 / 아니면 해당 프로세스 실행
        if any(q[1] < p[1] for p in queue):
            queue.append(q)
        else :
            answer.append(q)
    # location 실행 순서 찾기
    for a in answer:
        if a[0] == location:
            return answer.index(a) + 1