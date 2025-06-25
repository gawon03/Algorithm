from collections import deque
import copy

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

# 남, 동, 북, 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 감시해야하는 모든 방향
direction = {
    1 : [[0], [1], [2], [3]],
    2 : [[0, 2], [1, 3]],
    3 : [[0, 1], [1, 2], [2, 3], [3, 0]],
    4 : [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5 : [[0, 1, 2, 3]]
}

# 사무실의 범위를 벗어나는지 체크해주는 함수
def check(row, col):
    return row < 0 or row >= N or col < 0 or col >= M

# cctv 번호, 좌표 저장
def init():
    obj = deque()
    answer = 0
    for i in range(N):
        for j in range(M):
            # 벽이 아니고 빈칸이 아니면
            if space[i][j] != 6 and space[i][j] != 0:
                obj.append((space[i][j], i, j)) # cctv번호, cctv 좌표 저장
            # cctv가 아예 없는 경우도 고려해서 빈칸의 개수로 맞춰둠
            if space[i][j] == 0 : answer += 1
    return obj, answer

# cctv 좌표들, 빈칸 개수 초기화
cctv, answer = init()

def move(x, y, direc, space_copy):
    # 각각의 방향에 대해서 전부 이동시켜줌
    for d in direc :
        nx, ny = x, y

        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위를 벗어났거나 벽을 만났다면
            if check(nx, ny) or space_copy[nx][ny] == 6:
                break
            # 빈칸이 아니라면
            if space_copy[nx][ny] != 0:
                continue
            space_copy[nx][ny] = '#'


# 사각지대를 구하는 함수
def zero_cnt(space_copy):
    global answer
    cnt = 0
    for i in space_copy:
        cnt += i.count(0)
    answer = min(answer, cnt)


def dfs(level, space):
    space_copy = copy.deepcopy(space)

    if level == len(cctv):
        zero_cnt(space_copy)
        return

    number, x, y = cctv[level]

    # number번째 cctv에 대해 가능한 모든 방향을 순차적으로 고려
    for d in direction[number]:
        move(x, y, d, space_copy)
        dfs(level+1, space_copy) # level+1번째 cctv를 고려
        space_copy = copy.deepcopy(space)

        # 하나의 상태를 return한 다음 바로 전 상태로 바꿈
        # 만약 2번째 상태가 끝났다면, 1번째를 수행했을 때의 결과로 바꿈

dfs(0, space)
print(answer)