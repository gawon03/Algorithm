import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        answer += 1
        mix = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, mix)
        
    return answer