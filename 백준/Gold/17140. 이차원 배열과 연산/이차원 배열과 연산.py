from collections import Counter
from functools import reduce

def sortR(array):
    mx = 0 # 가장 긴 리스트의 길이
    for i in range(len(array)):
        X = Counter(array[i])
        del X[0] # 수를 정렬할 때, 0은 제외
        X = list(X.items())
        X.sort(key = lambda x : (x[1], x[0]))
        if len(X) > 50 : X = X[:50] # 크기가 100을 넘기면 안됨
        array[i] = reduce(lambda x, y : list(x) + list(y), X[1:], list(X[0])) # 2중 구조의 튜플을 1중 리스트화
        mx = max(mx, len(array[i]))

    # 가장 긴 리스트에 맞춰, 0 추가
    for i in range(len(array)):
        if len(array[i]) < mx:
            array[i].extend([0]*(mx-len(array[i])))

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

answer = 0
for _ in range(101):

    # 종료 조건
    if R <= len(board) and C <= len(board[0]) and board[R-1][C-1] == K :
        print(answer)
        break
    if answer == 100:
        print(-1)
        break

    answer += 1

    if len(board) >= len(board[0]) : # 행 개수 >= 열 개수
        sortR(board)
    else :
        board = list(map(list, zip(*board)))
        sortR(board)
        board = list(map(list, zip(*board)))