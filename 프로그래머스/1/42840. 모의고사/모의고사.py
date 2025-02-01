def solution(answers):
    n = len(answers)
    one = '12345'*(n//5+1)
    two = '21232425'*(n//8+1)
    three = '3311224455'*(n//10+1)
    result = [0, 0, 0]
    for i in range(n):
        if answers[i] == int(one[i]):
            result[0] += 1
        if answers[i] == int(two[i]):
            result[1] += 1
        if answers[i] == int(three[i]):
            result[2] += 1
    m = max(result)
    return [i+1 for i in range(3) if result[i] == m]