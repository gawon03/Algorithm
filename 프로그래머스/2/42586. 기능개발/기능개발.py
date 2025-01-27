# (answer[-1:], (100 - progresses[i])//speeds[i] + 1)


def solution(progresses, speeds):
    answer = []
    days = 0
    for p, s in zip(progresses, speeds):
        if days >= (100 - p)//s + 1*((100 - p)%s!=0):
            answer[-1] += 1
        else : 
            answer.append(1)
        days = max(days, (100 - p)//s + 1*((100 - p)%s!=0))
    return answer