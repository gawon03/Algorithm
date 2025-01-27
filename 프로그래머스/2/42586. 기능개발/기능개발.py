def solution(progresses, speeds):
    answer = []
    days = 0
    for p, s in zip(progresses, speeds):
        if days >= -((p-100)//s): # math.ceil((100-p)//s)과 동일
            answer[-1] += 1
        else : 
            answer.append(1)
            days = -((p-100)//s)
    return answer