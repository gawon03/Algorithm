from collections import deque

wheels = [deque(list(map(int, input()))) for _ in range(4)]

# 회전 횟수
k = int(input())

# [바퀴 번호, 회전 방향(1:시계, -1:반시계)]
move_lst = [list(map(int, input().split())) for _ in range(k)]

def move(idx, dir):
    global wheels

    # 시계 방향 회전
    if dir == 1:
        w = wheels[idx].pop()      # 마지막 원소를
        wheels[idx].appendleft(w)  # 첫 번째로 이동

    # 반시계 방향 회전
    else :
        w = wheels[idx].popleft()  # 첫 번째 원소를
        wheels[idx].append(w)      # 마지막으로 이동

    return

queue = deque()
visited = [False]*4

for n, d in move_lst:
    queue.append([n, d])
    visited = [False]*4
    while queue:
        num, dir = queue.popleft()

        temp = num-1
        left = num-2
        right = num

        if right <= 3 : # 오른쪽 확인
            if visited[right] != True and wheels[temp][2] != wheels[right][6]:
                queue.append([right+1, dir*-1])

        if left >= 0: # 왼쪽 확인
            if visited[left] != True and wheels[temp][6] != wheels[left][2]:
                queue.append([left+1, dir*-1])

        move(temp, dir)
        visited[temp] = True

answer = 0
for i in range(4):
    answer += wheels[i][0]*(2**i)

print(answer)