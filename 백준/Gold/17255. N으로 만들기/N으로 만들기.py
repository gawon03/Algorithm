N = input()

nums = list(N)
visited = dict()
answer = 0

# 현재 상태(case), 맨 앞 인덱스(left), 맨 뒤 인덱스(right), 현재까지 오면서 나온 숫자들을 이어붙인 문자열(seque)
def solution(case, left, right, seque):
    if case == N and seque not in visited:
        visited[seque] = 0 # seque들이 저장된 dictionary
        global answer
        answer += 1

    else:
        if left > 0: # 앞쪽에 붙일 숫자가 남았다면
            solution(nums[left-1]+case, left-1, right, seque+case)

        if right < len(nums)-1: # 뒤쪽에 붙일 숫자가 남았다면
            solution(case+nums[right+1], left, right+1, seque+case)

for i in range(len(nums)):
    solution(nums[i], i, i, nums[i])

print(answer)