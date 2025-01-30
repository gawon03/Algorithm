from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        sec = 0
        p = prices.popleft()
        for i in prices:
            sec += 1
            if i < p:
                break
        answer.append(sec)
    return answer