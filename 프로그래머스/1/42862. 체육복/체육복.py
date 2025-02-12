def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    union = set(lost)&set(reserve)
    idx = 0; cnt =0
    
    for r in reserve:
        if r not in union :
            for i in range(idx, len(lost)):
                if (abs(r-lost[i]) == 1) & (lost[i] not in union):
                    idx = i + 1
                    cnt += 1
                    break
    
    return n - len(lost) + cnt + len(list(union))




