# 하나씩 확인하면서 
# index+1 >= c[index] 이면 c[index]
# c[-1] >= len(c) 이면 len(c)
# 

def solution(citations):    
    citations.sort(reverse = True)
    answer = 0
    for i in range(len(citations)):
        if citations[i]>=i+1:
            answer = i+1
    return answer
    