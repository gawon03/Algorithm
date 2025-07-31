# N, K 입력
N, K = map(int, input().split())

# 체스판 정보 입력
chess_info = [list(map(int, input().split())) for _ in range(N)]

# 체스판 말 위치 저장
horse_loc = [[[] for _ in range(N)] for _ in range(N)]

# 말의 정보 입력
horse_info = []

for i in range(K):
    row, col, dir = map(int, input().split())
    # 리스트에 추가
    horse_info.append([row-1, col-1, dir-1])
    # 체스판에 말 위치 저장
    horse_loc[row-1][col-1].append(i)

# 4가지 이동 방향 정의 (0 : 오른쪽, 1 : 왼쪽, 2 : 위, 3 : 아래)
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 말 이동 함수 구현
def move_horse(i):
    x, y, dir = horse_info[i]
    # 이동
    nx, ny = x + moves[dir][0], y + moves[dir][1]

    # 범위 밖이거나 파란색인지 확인
    if not (0 <= nx < N and 0 <= ny < N) or chess_info[nx][ny] == 2:
        # 방향 전환 후 업데이트
        dir = (dir + 1) % 2 + (dir // 2) * 2  # 방향 반대로
        horse_info[i][2] = dir

        # 다음 한칸 진행
        nx, ny = x + moves[dir][0], y + moves[dir][1]
        # 다시 확인
        if not (0 <= nx < N and 0 <= ny < N) or chess_info[nx][ny] == 2:
            return 0

    # 같은 곳에 있는 말 모두 꺼내기
    idx = horse_loc[x][y].index(i)  # 이동할 말 인덱스 뽑아서
    move_together = horse_loc[x][y][idx:]  # 말이 이동할 때 위에 있는 말들도 같이 이동
    horse_loc[x][y] = horse_loc[x][y][:idx]

    # 흰색이면 말 추가
    if chess_info[nx][ny] == 0:
        horse_loc[nx][ny].extend(move_together)

    # 빨간색일 경우 쌓인 순서 반대
    if chess_info[nx][ny] == 1:
        horse_loc[nx][ny].extend(move_together[::-1])

    # 말 위치 업데이트
    for h in move_together:
        horse_info[h][0] = nx
        horse_info[h][1] = ny

    # 쌓인 말 4개면 종료
    if len(horse_loc[nx][ny]) >= 4:
        return 1

    return 0


# 결과 출력
def solution():
    turn = 1
    while turn <= 1000:
        for i in range(K):
            flag = move_horse(i)
            if flag:
                return turn  # 결과 반환하고 함수 종료
        turn += 1
    return -1  # 1000턴 이내 종료 조건 없으면 -1 반환

result = solution()
print(result)
