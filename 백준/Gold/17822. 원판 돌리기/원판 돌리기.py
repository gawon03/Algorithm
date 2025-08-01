from collections import deque
import copy

# 원판 개수 = 반지름 최대 길이(N), 정수 개수(M), 회전 수(T)
N, M, T = map(int, input().split())

# 원판에 적힌 수 정보 : i번째 줄의 j번째 수
circles = [deque(list(map(int, input().split()))) for _ in range(N)]

# 회전 방법 : x(배수), d(0:시계, 1:반시계), k(회전 칸수)
method = [list(map(int, input().split())) for _ in range(T)]


# 회전 함수
def rotate(x, d, k):
    for i in range(x - 1, N, x):
        if d == 0:
            circles[i].rotate(k)   # 시계
        else:
            circles[i].rotate(-k)  # 반시계

# 인접 수 제거 함수
def remove_adjacent():
    removed = False
    to_remove = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if circles[i][j] == 0:
                continue

            curr = circles[i][j]

            # 인접 확인: 오른쪽, 왼쪽, 위, 아래 (원형 구조 주의)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni = i + dx
                nj = (j + dy) % M

                if 0 <= ni < N and circles[ni][nj] == curr:
                    to_remove[i][j] = True
                    to_remove[ni][nj] = True
                    removed = True

    # 실제 제거
    for i in range(N):
        for j in range(M):
            if to_remove[i][j]:
                circles[i][j] = 0

    return removed

# 평균 계산 및 조정
def calculate():
    total = 0
    count = 0

    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                total += circles[i][j]
                count += 1

    if count == 0:
        return

    avg = total / count

    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                if circles[i][j] > avg:
                    circles[i][j] -= 1
                elif circles[i][j] < avg:
                    circles[i][j] += 1

# 수가 남아있는지 체크
def has_numbers():
    for i in range(N):
        for j in range(M):
            if circles[i][j] != 0:
                return True
    return False

# T번 회전 및 처리
for x, d, k in method:
    rotate(x, d, k)

    if not remove_adjacent():
        calculate()

# 결과 출력
result = sum(sum(row) for row in circles)
print(result)