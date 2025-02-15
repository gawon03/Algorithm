def solution(routes):
    routes.sort(key = lambda x : x[0])
    answer = 0
    while routes :
        temp = routes.pop()
        answer += 1
        for r in routes[::-1]:
            if r[1] >= temp[0]:
                routes.pop()
            else : 
                break
    return answer