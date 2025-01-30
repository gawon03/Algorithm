from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights) 
    bridge = deque([0] * bridge_length)   # 다리
    onbridge = 0                          # 다리 위 트럭 하중
    answer = 0                            # 시간
    
    # 다리 위의 트럭이 없을 때까지(= 모든 트럭이 다리를 건널 때까지)
    while bridge:
        answer += 1
        onbridge -= bridge.popleft() # 맨 앞에 위치한 트럭이 다리를 지나면 하중 감소
        
        # 남은 대기 트럭이 있으면
        if truck_weights:
            # 다리 위 트럭의 무게 + 새로운 트럭 <= 다리가 견딜 수 있는 무게이면
            if onbridge + truck_weights[0] <= weight:   # 대기 트럭에서 출발
                truck = truck_weights.popleft()         # 다리에 새로운 트럭 추가
                bridge.append(truck)                    # 새로운 트럭만큼 다리 하중 증가
                onbridge += truck
                
            # 그렇지 않으면
            else:
                bridge.append(0)                        # 다리에 0을 추가해서 자리 이동 표시
        
    return answer