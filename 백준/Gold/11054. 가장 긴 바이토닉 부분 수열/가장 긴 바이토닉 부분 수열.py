N = int(input())
array = list(map(int, input().split()))
array_reverse = array[::-1]

LIS = [1]*N
LDS = [1]*N

# 부분 수열의 길이 최댓값
for i in range(N):
    for k in range(i):
        if array[i] > array[k]:
            LIS[i] = max(LIS[i], LIS[k]+1)
        if array_reverse[i] > array_reverse[k]:
            LDS[i] = max(LDS[i], LDS[k]+1)

# i를 봉우리로 하는 경우의 최댓값
ans = 0
for i in range(N):
    ans = max(ans, LIS[i] + LDS[N-i-1] - 1)
print(ans)