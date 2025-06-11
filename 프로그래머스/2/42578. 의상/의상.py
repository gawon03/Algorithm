def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    clothes_type = {}
    for c, t in clothes:
        clothes_type[t] = clothes_type.get(t, 0) + 1
    
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for t in clothes_type:
        answer *= (clothes_type[t]+1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1