# arr 하나씩 pop
# answer의 마지막 원소랑 다르면 append

def solution(arr):
    answer = [arr[-1]]
    arr = arr[:-1]
    for _ in range(len(arr)):
        a = arr.pop()
        if answer[-1] != a :
            answer.append(a)
    return answer[::-1]