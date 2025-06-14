n = int(input()) # 보드 크기
k = int(input()) # 사과 개수

# 사과 위치(행, 열)
apple_idx = [list(map(int, input().split())) for _ in range(k)]

# 방향 변환 횟수
l = int(input())

# 방향 변환 정보
# 게임 시작으로부터 X초가 끝난 뒤에 C(L|D)방향으로 회전
# L:왼쪽으로 90도 회전, D:오른쪽으로 90도 회전
d = [list(input().split()) for _ in range(l)]

# 뱀은 [0,0]에서 출발, 몸 길이 : 1, 오른쪽으로 이동

# 뱀의 몸 인덱스 리스트
# 머리 먼저 이동하여 추가, 꼬리 삭제
# 머리 이동 경우의 수(사과 위치, 벽 위치, 자기 몸 위치, 그 외)
# 1. 사과가 위치 : 이동 방향에 머리 추가
# 2. 벽 위치 or 자기 몸 위치 : 게임 종료 후 시간 출력
# 3. 그 외 : 이동 방향에 머리 추가 and 꼬리 삭제

from collections import deque

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(snake, dir_, ld, sec, stat):
  hx, hy = snake[0]
  tx, ty = snake[-1]
  sec += 1
  if ld == 'L': # 왼쪽으로 회전
    dir_ -= 1
    if dir_ == -1:
      dir_ = 3
  elif ld == 'D': # 오른쪽으로 회전
    dir_ += 1
    if dir_ == 4:
      dir_ = 0
  ld = 'S' # 회전 여부 초기화

  nhx = hx + dx[dir_]
  nhy = hy + dy[dir_]

  # 이동한 머리가 벽 또는 자기 몸일 때 게임 종료
  if nhx < 0 or nhx >= n or nhy < 0 or nhy >= n or [nhx, nhy] in snake:
    stat = True
    return snake, dir_, ld, sec, stat
  else:
    snake.appendleft([nhx, nhy]) # 머리 추가
    if [nhx+1, nhy+1] in apple_idx:  # 만약 사과라면
      apple_idx.remove([nhx+1, nhy+1]) # 사과를 먹고
    else :  # 사과 안 먹었으면 꼬리 제거
      snake.pop()
    return snake, dir_, ld, sec, stat


def solution():
  snake = deque([[0,0]])
  i = 0
  if i < l:
    x, c = d[i][0], d[i][1]
  sec = 0
  dir_ = 1 # 오른쪽
  ld = 'S'; stat = False
  while True:
    if i < l :
      if sec == int(x):
        sec = int(x)
        ld = c
        if i < l-1:
          i += 1
          x, c = d[i][0], d[i][1]
    snake, dir_, ld, sec, stat = move(snake, dir_, ld, sec, stat)
    if stat == True:
      break

  return print(sec)

solution()