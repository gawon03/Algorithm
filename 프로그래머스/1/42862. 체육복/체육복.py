# n = 12
# lost = [3, 5, 7]
# reserve = [2, 4, 6, 11]
# [2, 4, 6]
# return = 12
# 빌릴 수 있는 체육복이 적은 학생부터 선택 
# reserve에서 하나씩 확인
# 만약 lost에 자기 자신이 있으면 패스, 없으면 lost에서 학생 빌려주고 lost에서 제거
# 

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




