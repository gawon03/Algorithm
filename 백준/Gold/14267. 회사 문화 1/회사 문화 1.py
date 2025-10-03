# 회사의 직원 수(n), 최초의 칭찬의 횟수(m)
n, m = map(int, input().split())

# 직속 상사의 번호(작을수록 높음. 1번이 사장)
grade = [0] + list(map(int, input().split()))

# good[i] = i번 직원이 받은 칭찬 점수
good = [0] * (n+1)
for _ in range(m):
    s, p = map(int, input().split())
    good[s] += p

for i in range(2, n+1):
    good[i] += good[grade[i]]

print(*good[1:])