def solution(money):
    answer = 0

    dp1 = [] # 첫 집을 털었을 때
    dp2 = [] # 첫 집을 안 털고 두 번째 집을 털었을 때

    dp1.append(money[0])
    dp2.append(0)
    dp1.append(dp1[0])
    dp2.append(money[1])

    for i in range(2, len(money) - 1):
        dp1.append(max(dp1[i - 1], dp1[i - 2] + money[i]))
        dp2.append(max(dp2[i - 1], dp2[i - 2] + money[i]))
    e = len(money) - 1
    dp1.append(dp1[e - 1])
    dp2.append(max(dp2[e - 1], dp2[e - 2] + money[e]))

    answer = max(dp1[e], dp2[e])

    return answer