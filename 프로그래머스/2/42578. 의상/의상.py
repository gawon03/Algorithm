def solution(clothes):
    clothes_type = {}
    for c, t in clothes :
        clothes_type[t] = clothes_type.get(t, 0) + 1
        
    answer = 1
    for t in clothes_type:
        answer *= (clothes_type[t]+1)
        print(t)
    return answer -1
    
    
    
    return answer