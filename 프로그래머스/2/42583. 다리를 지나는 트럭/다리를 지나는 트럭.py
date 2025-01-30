from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    onbridge = 0
    answer = 0
    
    while bridge:
        answer += 1
        onbridge -= bridge.popleft()
        
        if truck_weights:
            if onbridge + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                onbridge += truck
            else:
                bridge.append(0)
        
    return answer