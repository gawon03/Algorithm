import sys
from itertools import permutations

#(1) 순열만들기
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
p = list(permutations(arr, n))

answer = 0
for i in p:
    s = 0
# (2) 반복문으로 튜플을 꺼내 각 순열마다 차이의 합(s)을 구하고, 최대값을 answer에 저장한다
    for j in range(n-1):
        s += abs(i[j] - i[j+1])
# 모든 경우 원소들끼리의 차이의 절댓값의 합을 max함수를 이용하여 갱신
    answer = max(answer, s)

print(answer)
