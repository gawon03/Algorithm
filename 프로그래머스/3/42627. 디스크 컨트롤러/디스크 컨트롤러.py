import heapq

def solution(jobs):
    answer = 0
    now = 0    # 현재 시간
    i = 0      # 처리된 작업 개수
    start = -1 # 마지막으로 완료된 작업 시간
    heap = []  # 실행 가능한 작업을 저장하는 최소 힙
    # 모든 작업을 처리할 때까지 반복
    while i < len(jobs): 
        # job 리스트를 하나씩 확인하면서 현재 실행할 수 있는 작업을 힙에 추가
        for job in jobs:             
            if start < job[0] <= now:  # 이전 작업 완료 이후에 요청된 작업만 추가(이미 처리된 작업 힙추가 방지)
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap:
            current = heapq.heappop(heap)
            start = now   # 작업 수행 시작 시간
            now += current[0] # 작업 수행 끝난 시간
            answer += now - current[1] # 요청된 시각부터 현재까지 걸린 시간
            i += 1 # 처리된 작업 개수 증가
        else:
            now += 1 # 실행할 작업이 없으면 1 증가
            
    return answer // len(jobs)