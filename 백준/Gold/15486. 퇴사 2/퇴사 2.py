N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]

amt = [0]*N
for i in range(N):

    # 상담 소요 기간(t), 상담 금액(p)
    t, p = counsel[i]
    # 상담 완료일
    idx = i + t -1

    if i != 0:
        temp = amt[i-1]
    else:
        temp = 0

    amt[i] = max(amt[i], temp)

    if 0<=idx<=N-1:
        amt[idx] = max(amt[idx], temp+p)

print(amt[-1])