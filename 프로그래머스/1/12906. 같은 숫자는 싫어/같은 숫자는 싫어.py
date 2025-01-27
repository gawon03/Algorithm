def solution(arr):
    answer = []
    for a in arr:
        if answer[-1:] != [a] :
            answer.append(a)
    return answer